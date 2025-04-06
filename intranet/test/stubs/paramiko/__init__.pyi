# Stubs for paramiko (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from paramiko.transport import SecurityOptions as SecurityOptions, Transport as Transport
from paramiko.client import SSHClient as SSHClient, MissingHostKeyPolicy as MissingHostKeyPolicy, AutoAddPolicy as AutoAddPolicy, RejectPolicy as RejectPolicy, WarningPolicy as WarningPolicy
from paramiko.channel import Channel as Channel
from paramiko.ssh_exception import SSHException as SSHException, PasswordRequiredException as PasswordRequiredException, BadAuthenticationType as BadAuthenticationType, ChannelException as ChannelException, BadHostKeyException as BadHostKeyException, AuthenticationException as AuthenticationException, ProxyCommandFailure as ProxyCommandFailure
from paramiko.server import ServerInterface as ServerInterface, SubsystemHandler as SubsystemHandler
from paramiko.rsakey import RSAKey as RSAKey
from paramiko.dsskey import DSSKey as DSSKey
from paramiko.sftp import SFTPError as SFTPError
from paramiko.sftp_client import SFTP as SFTP, SFTPClient as SFTPClient
from paramiko.sftp_server import SFTPServer as SFTPServer
from paramiko.sftp_attr import SFTPAttributes as SFTPAttributes
from paramiko.sftp_handle import SFTPHandle as SFTPHandle
from paramiko.sftp_si import SFTPServerInterface as SFTPServerInterface
from paramiko.sftp_file import SFTPFile as SFTPFile
from paramiko.message import Message as Message
from paramiko.file import BufferedFile as BufferedFile
from paramiko.agent import Agent as Agent, AgentKey as AgentKey
from paramiko.pkey import PKey as PKey
from paramiko.hostkeys import HostKeys as HostKeys
from paramiko.config import SSHConfig as SSHConfig
from paramiko.proxy import ProxyCommand as ProxyCommand
from paramiko.common import io_sleep as io_sleep

# Names in __all__ with no definition:
#   util
