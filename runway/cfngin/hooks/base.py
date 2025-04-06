"""Base class for CFNgin hooks."""
import logging

from troposphere import Tags
from six.moves import UserDict

from runway.util import MutableMap

from ..actions import build
from ..exceptions import StackFailed
from ..plan import COLOR_CODES
from ..stack import Stack
from ..status import COMPLETE, FAILED, PENDING, SKIPPED, SUBMITTED

LOGGER = logging.getLogger(__name__)


class Hook(object):
    """Base class for hooks.

    Not all hooks need to be classes and not all classes need to be hooks.

    Attributes:
        args (MutableMap): Keyword arguments passed to the hook, loaded into
            a MutableMap object.
        blueprint (Optional[Blueprint]): Blueprint generated by the hook if
            it will be deploying a stack.
        context (Context): Context instance. (passed in by CFNgin)
        provider (BaseProvider): Provider instance. (passed in by CFNgin)
        stack (Optional[Stack]): Stack object if the hook deploys a stack.
        stack_name (str): Name of the stack created by the hook if a stack is
            to be created.

    """

    def __init__(self, context, provider, **kwargs):
        """Instantiate class.

        Args:
            context (:class:`runway.cfngin.context.Context`): Context instance.
                (passed in by CFNgin)
            provider (:class:`runway.cfngin.providers.base.BaseProvider`):
                Provider instance. (passed in by CFNgin)

        """
        kwargs.setdefault('tags', {})

        self.args = MutableMap(**kwargs)
        self.args.tags.update(context.tags)
        self.blueprint = None
        self.context = context
        self.provider = provider
        self.stack = None
        self.stack_name = 'stack'
        self._deploy_action = HookBuildAction(self.context, self.provider)
        self._destroy_action = HookDestroyAction(self.context, self.provider)

    @property
    def tags(self):
        """Return tags that should be applied to any resource being created.

        Returns:
            troposphere.Tags

        """
        return Tags(**dict(self.context.tags, **self.args.tags.data))

    def generate_stack(self, **kwargs):
        """Create a CFNgin Stack object.

        Returns:
            Stack

        """
        definition = HookStackDefinition(name=self.stack_name,
                                         tags=self.args.tags.data,
                                         **kwargs)
        stack = Stack(definition, self.context)
        stack._blueprint = self.blueprint  # pylint: disable=protected-access
        return stack

    def get_template_description(self, suffix=None):
        """Generate a template description.

        Args:
            suffix (Optional[str]): Suffix to append to the end of a
                CloudFormation template description.

        Returns:
            str: CloudFormation template description.

        """
        template = 'Automatically generated by {}'
        if suffix:
            template += ' - {}'
            return template.format(self.__class__.__module__, suffix)
        return template.format(self.__class__.__module__)

    def deploy_stack(self, stack=None, wait=False):
        """Deploy a stack.

        Args:
            stack (Optional[Stack]): A stack to act on.
            wait (bool): Wither to wait for the stack to complete before
                returning.

        Returns:
            Status: Ending status of the stack.

        """
        return self._run_stack_action(action=self._deploy_action,
                                      stack=stack,
                                      wait=wait)

    def destroy_stack(self, stack=None, wait=None):
        """Destroy a stack.

        Args:
            stack (Optional[Stack]): A stack to act on.
            wait (bool): Wither to wait for the stack to complete before
                returning.

        Returns:
            Status: Ending status of the stack.

        """
        return self._run_stack_action(action=self._destroy_action,
                                      stack=stack,
                                      wait=wait)

    def post_deploy(self):
        """Run during the **post_deploy** stage."""
        raise NotImplementedError

    def post_destroy(self):
        """Run during the **post_destroy** stage."""
        raise NotImplementedError

    def pre_deploy(self):
        """Run during the **pre_deploy** stage."""
        raise NotImplementedError

    def pre_destroy(self):
        """Run during the **pre_destroy** stage."""
        raise NotImplementedError

    @staticmethod
    def _log_stack(stack, status):
        """Log stack status. Mimics normal stack deployment.

        Args:
            stack (:class:`runway.cfngin.stack.Stack`): The stack being logged.
            status (:class:`runway.cfngin.status.Status`) The status being
                logged.

        """
        msg = "%s: %s" % (stack.name, status.name)
        if status.reason:
            msg += " (%s)" % (status.reason)
        color_code = COLOR_CODES.get(status.code, 37)
        LOGGER.info(msg, extra={"color": color_code})

    def _run_stack_action(self, action, stack=None, wait=None):
        """Run a CFNgin hook modified for use in hooks.

        Args:
            action (BaseAction): Action to be taken against a stack.
            stack (Optional[Stack]): A stack to act on.
            wait (bool): Wither to wait for the stack to complete before
                returning.

        Returns:
            Status: Ending status of the stack.

        """
        stack = stack or self.stack
        status = action.run(stack=stack, status=PENDING)
        self._log_stack(stack, status)

        if wait and status != SKIPPED:
            status = self._wait_for_stack(action=action, stack=stack,
                                          last_status=status)
        return status

    def _wait_for_stack(self, action, last_status=None, stack=None,
                        till_reason=None):
        """Wait for a CloudFormation stack to complete.

        Args:
            action (BaseAction): Action to be taken against a stack.
            last_status (Optional[Status]): The last status of the stack.
            stack (Optional[Stack]): A stack that has been acted upon.
            till_reason (Optional[str]): Status string to wait for before
                returning. ``COMPLETE`` or ``FAILED`` status will return
                before this condition if found.

        Returns:
            Status: Ending status of the stack.

        Raises:
            StackFailed: Stack is in a failed state.

        """
        status = last_status or SUBMITTED
        stack = stack or self.stack

        while True:
            if status in (COMPLETE, FAILED):
                break
            if (till_reason and status.reason) and status.reason == till_reason:
                break
            if last_status and last_status.reason != status.reason:
                # log status changes like rollback
                self._log_stack(stack, status)
                last_status = status
            LOGGER.debug('Waiting for stack to complete...')
            status = action.run(stack=stack, status=status)

        self._log_stack(stack, status)
        if status == FAILED:
            raise StackFailed(stack_name=stack.fqn,
                              status_reason=status.reason)
        return status


class HookBuildAction(build.Action):
    """Build action that can be used from hooks."""

    def __init__(self, context, provider):
        """Instantiate class.

        Args:
            context (:class:`runway.cfngin.context.Context`): The context
                for the current run.

        """
        super(HookBuildAction, self).__init__(context)
        self._provider = provider

    @property
    def provider(self):
        """Override the inherited property to return the local provider."""
        return self._provider

    def build_provider(self, stack):
        """Override the inherited method to always return local provider."""
        return self._provider

    def run(self, **kwargs):
        """Run the action for one stack."""
        return self._launch_stack(**kwargs)


# the build action has logic to destroy stacks so we can just extend the
# HookBuildAction and change `run` in use the `_destroy_stack` method instead
class HookDestroyAction(HookBuildAction):
    """Destroy action that can be used from hooks."""

    def run(self, **kwargs):
        """Run the action for one stack."""
        return self._destroy_stack(**kwargs)


# TODO remove multiple inheritance when droping python 2 support
class HookStackDefinition(UserDict, object):
    """Stack definition for use in hooks to avoid cyclic imports."""

    def __init__(self, name, **kwargs):
        """Instantiate class."""
        values = {
            'class_path': None,
            'enabled': True,
            'in_progress_behavior': None,
            'name': name,
            'locked': False,
            'profile': None,
            'protected': False,
            'region': None,
            'required_by': None,
            'requires': None,
            'stack_name': None,
            'stack_policy_path': None,
            'tags': None,
            'template_path': None,
            'termination_protection': False,
            'variables': None
        }
        values.update(kwargs)
        super(HookStackDefinition, self).__init__(**values)

    def __getattr__(self, key):
        """Implement dot notation."""
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)
