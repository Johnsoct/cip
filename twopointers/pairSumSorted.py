from typing import List

def main(nums: List[int], target: int) -> List[int]:
    """Uses two pointers and inward traversal to find a pair of indexes which equal target."""
    left = 0
    pairs = []
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pairs = [left, right]

            break
        elif sum > target:
            right -= 1
        else:
            left += 1

    return pairs

def test_main():
    # From the exercise
    assert main([-5, -2, 3, 4, 6], 7) == [2, 3]
    assert main([1, 1, 1], 2) == [0, 2]
    assert main([], 0) == []
    assert main([1], 1) == []
    assert main([2, 3], 5) == [0, 1]
    assert main([2, 4], 5) == []
    assert main([2, 2, 3], 5) == [0, 2]
    assert main([-1, 2, 3], 2) == [0, 2]
    assert main([-3, -2, -1], -5) == [0, 1]
