from typing import List

def find_median_from_two_sorted_arrays(
    nums1: List[int],
    nums2: List[int],
) -> float:
    # Ensure `arr1` is the smallest array to minimize the search space
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)
    half_total_len = (m + n) // 2 # Will prefer the left "median" if of even length
    left = 0
    right = m - 1

    # Since a median always exists in a non-empty array, continue until it's found
    while True:
        L1_index = (left + right) // 2
        L2_index = half_total_len - (L1_index + 1) - 1
        # If out of bounds, set to (+/-)infinity
        L1 = float("-inf") if L1_index < 0 else nums1[L1_index]
        R1 = float("inf") if L1_index >= m - 1 else nums1[L1_index + 1]
        L2 = float("-inf") if L2_index < 0 else nums2[L2_index]
        R2 = float("inf") if L2_index >= n - 1 else nums2[L2_index + 1]

        # If L1 > R2, L1 is too far to the right
        if L1 > R2:
            right = L1_index - 1

        # If L2 > R1, L1 is too far to the left
        elif L2 > R1:
            left = L1_index + 1

        # If L1 and L2 <= R1 and R2, we found the correct slice
        else:
            # If the length of the two arrays is even, calculate the median
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2.0
            # If the length of the two arrays is odd, ... select the median
            else:
                return min(R1, R2)

def test():
    assert find_median_from_two_sorted_arrays([], [1]) == 1.0
    assert find_median_from_two_sorted_arrays([1], []) == 1.0
    assert find_median_from_two_sorted_arrays([0, 2, 5, 6, 8], [1, 3, 7]) == 4.0
    assert find_median_from_two_sorted_arrays([0, 2, 5, 6, 8], [1, 3, 7, 9]) == 5.0
