from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame


class QuotaShare:
    def __init__(
            self,
            ret: float
    ):

        self.ret = ret

    def apply_bdx(
            self,
            bdx: DataFrame
    ):

        bdx['Retained Premium'] = bdx['Premium'] * self.ret
        bdx['Retained Loss'] = bdx['Loss'] * self.ret
        bdx['Ceded Loss'] = bdx['Loss'] * (1 - self.ret)
        bdx['Ceded Premium'] = bdx['Premium'] * (1 - self.ret)
