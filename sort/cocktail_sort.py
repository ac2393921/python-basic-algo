"""cocktailソート"""

from typing import List


def cocktail_sort(numbers: List[int]) -> List[int]:
    """Listをcocktailソートで並べ替える

    Args:
        numbers(List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1

    while swapped:
        # 右方向
        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break

        # 左方向
        swapped = False
        end -= 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start += 1

    return numbers
