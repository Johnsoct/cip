from typing import List

def find_lower_bound(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left = 0
    # Since we're looking for the lower bounds, we don't need to extend right to len(nums)
    right = len(nums) - 1
 
    while left < right:
        mid = left + (right - left) // 2

        # Slide the window to the left
        if nums[mid] > target:
            right = mid - 1

        # Slide the window to the right
        elif nums[mid] < target:
            left = mid + 1

        # Slide the window to the left (when left and mid are equal)
        else:
            right = mid

    if nums[left] == target:
        return left

    else:
        return -1

def find_upper_bound(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left = 0
    # Since we're looking for the lower bounds, we don't need to extend right to len(nums)
    right = len(nums) - 1
 
    while left < right:
        # mid is biased towards the right instead of left which in combination with excluding mid
        # when setting right to mid - 1 prevents an infinite loop when setting left = mid
        mid = left + (right - left) // 2 + 1

        # Slide the window to the left
        if nums[mid] > target:
            right = mid - 1

        # Slide the window to the right
        elif nums[mid] < target:
            left = mid + 1

        # Slide the window to the right (when target and mid are equal)
        else:
            left = mid

    if nums[right] == target:
        return right 

    else:
        return -1

def find_first_and_last_occurence(nums: List[int], target: int) -> List[int]:
    lower_bounds = find_lower_bound(nums, target)
    upper_bounds = find_upper_bound(nums, target)

    return [
        lower_bounds,
        upper_bounds,
    ]

def test():
    nums = [ 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11 ]

    assert find_lower_bound([], 4) == -1
    assert find_lower_bound(nums, 4) == 3
    assert find_upper_bound(nums, 4) == 5
    assert find_upper_bound(nums, 9) == 10
    assert find_first_and_last_occurence(nums, 4) == [ 3, 5 ]
