from typing import Tuple


class SlidingScale:
    def __init__(
            self,
            rules: Tuple[
                list,  # commission values
                list,  # loss ratios
                list  # increments
            ]
    ):

        self.rules = rules

        self.validate_rules()

    def __repr__(self):

        name_list = [
            'Minimum Commission',
            'Sliding 1:1 to',
            'Sliding .5:1 to a Maximum'
        ]

        value_list = [
            '25% at a 60% current year loss ratio',
            '35% at a 50% current year loss ratio',
            '45% at a 30% current year loss ratio'
        ]

        padding1 = max([len(x) for x in name_list]) + 1
        padding2 = 16

        res = ''

        for name, value in zip(name_list, value_list):
            res += '\n' + f'{name + ":":<{padding1}}\t{value:>{padding2}}'

        return res

    def validate_rules(self) -> None:

        if len(self.rules[0]) != len(self.rules[1]):
            raise AttributeError("The number of commission ratios need to match the number of loss ratios.")

        if not (len(self.rules[0]) - len(self.rules[2]) == 1):
            raise AttributeError(
                "The number of increments need to be one less than the number of commission or loss ratios"
            )


# class SlidingScaleRule:
#     def __init__(self):
