"""selectionソート"""


from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    """Listをselectionソートで並べ替える

    Args:
        numbers (List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    len_numbers = len(numbers)

    for i in range(numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers
