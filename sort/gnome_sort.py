"""gnomeソート"""


from typing import List


def gnome_sort(numbers: List[int]) -> List[int]:
    """Listをgnome_sortソートで並べ替える

    Args:
        numbers (List[int]): 並べ替えをするintのリスト

    Returns:
        List[int]: sort後のリスト

    """
    len_numbers = len(numbers)
    idx = 0

    while idx < len_numbers:
        if idx == 0:
            idx += 1
        if numbers[idx] >= numbers[idx-1]:
            idx += 1
        else:
            numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
            idx -= 1

    return numbers
