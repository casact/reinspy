from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reinspy.occurrence import Occurrence


class Loss:
    def __init__(
            self,
            amount,
            occurrence: Occurrence = None
    ):

        self.amount = amount
        self.occurrence = occurrence
