"""bubbleソート"""

from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    """Listをbubbleソートで並べ替える

    Args:
        numbers (List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers - 1 + 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers
