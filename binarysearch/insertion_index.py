from typing import List

def find_insertion_index(nums: List[int], target: int) -> int:
    left = 0
    # Intentionally 1 past the last index as the "last" position would be the insertion if the
    # target does not exist
    right = len(nums)
 
    while left < right:
        mid = left + (right - left) // 2

        # slide the window to the left
        if nums[mid] >= target:
            right = mid

        # slide the window to the right
        else:
            left = mid + 1

    # left is always within the bounds of the array or the insertion index of the target's position
    # if it is greater than all the other values in the array
    return left

def test():
    assert find_insertion_index([ 1, 2, 4, 5, 7, 8, 9 ], 4) == 2
    assert find_insertion_index([ 1, 2, 4, 5, 7, 8, 9 ], 6) == 4
