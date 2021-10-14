"""bogoソート"""

import random
from typing import List


def __in_order(numbers: List[int]) -> bool:
    """intのリストが全てsortされているか判定

    Args:
        numbers(List[int]):  intのリスト

    Returns:
        bool: 全てsortされていればTrue

    """
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))


def bogo_sort(numbers: List[int]) -> List[int]:
    """

    Args:
        numbers(List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    while not __in_order(numbers):
        random.shuffle(numbers)
    random.shuffle(numbers)

    return numbers
