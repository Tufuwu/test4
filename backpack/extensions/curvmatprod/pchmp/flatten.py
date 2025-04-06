from backpack.core.derivatives.flatten import FlattenDerivatives
from backpack.extensions.curvmatprod.pchmp.pchmpbase import PCHMPBase


class PCHMPFlatten(PCHMPBase):
    def __init__(self):
        super().__init__(derivatives=FlattenDerivatives())

    def backpropagate(self, ext, module, grad_inp, grad_out, backproped):
        if self.derivatives.is_no_op(module):
            return backproped
        else:
            return super().backpropagate(ext, module, grad_inp, grad_out, backproped)
