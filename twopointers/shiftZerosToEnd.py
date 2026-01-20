from typing import List

def main(nums: List[int]) -> None:
    """Swaps positions within a List until all 0s have been moved to the end."""

    left = 0

    for right in range(len(nums)):
        # If right is not on a non-zero, move forward
        if (nums[right] != 0):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


def test_main():
    nums = [0, 1, 0, 3, 2]
    main(nums)
    assert(nums) == [ 1, 3, 2, 0, 0 ]
