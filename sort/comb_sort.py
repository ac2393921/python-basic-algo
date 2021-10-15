"""combソート"""


from typing import List


def comb_sort(numbers: List[int]) -> List[int]:
    """Listをcombソートで並べ替える

    Args:
        numbers (List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True

    return numbers

