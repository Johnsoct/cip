from typing import List


def find_the_target_in_a_rotated_sorted_array(
    nums: List[int],
    target: int,
) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        isLeftSubarraySorted = nums[left] <= nums[mid]
        IsTargetInLeftSubarray = nums[left] <= target < nums[mid]
        IsTargetInRightSubarray = nums[mid] < target <= nums[right]

        if nums[mid] == target:
            return mid

        if isLeftSubarraySorted:
            if IsTargetInLeftSubarray:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if IsTargetInRightSubarray:
                left = mid + 1
            else:
                right = mid - 1

    if nums and nums[left] == target:
        return left
    else:
        return -1


def test():
    assert find_the_target_in_a_rotated_sorted_array([], 1) == -1
    assert (
        find_the_target_in_a_rotated_sorted_array([8, 9, 1, 2, 3, 4, 5, 6, 7], 1) == 2
    )
