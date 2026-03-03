from typing import List

def is_enough(heights: List[int], target: int, cut_height: int) -> bool:
    cut_wood = 0

    for height in heights:
        if height > cut_height:
            cut_wood += height - cut_height

    return cut_wood >= target


def cutting_wood(heights: List[int], target: int) -> int:
    left = 0
    right = max(heights)

    while left < right:
        mid = left + (right - left) // 2 + 1

        if is_enough(heights, target, mid):
            left = mid
        else:
            right = mid - 1

    return right

def test():
    assert cutting_wood([2, 6, 3, 8], 7) == 3
