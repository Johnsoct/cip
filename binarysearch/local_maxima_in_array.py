from typing import List, Union

def find_local_maxima_in_array(nums: List[int]) -> Union[int, None]:
    """
    Finds and returns ANY local maxima in an array

    A local maxima is any value greater than both its immediate neighbors.
    """
    if not nums:
        return None

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

def test():
    assert find_local_maxima_in_array([]) == None
    assert find_local_maxima_in_array([ 1, 4, 3, 2, 3 ]) == 1
    assert find_local_maxima_in_array([ 1, 2, 3, 4, 5 ]) == 4
    assert find_local_maxima_in_array([ 1, 2, 3, 4, 3 ]) == 3
    assert find_local_maxima_in_array([ 1, 4, 3, 2, 1 ]) == 1
