from typing import List

def find_geometric_sequence_triplets(
    nums: List[int],
    ratio: int
) -> int:
    nums_hashset = set(nums)
    triplets = []

    for num in nums:
        # calculate x, x(r), and x(r^2)
        x = num
        xr = num * ratio
        xr2 = num * (ratio**2)

        print(x, xr, xr2)

        # Check if x(r) and x(r^2) are in nums_hashset
        in_hashset = xr in nums_hashset and xr2 in nums_hashset
        if not in_hashset:
            continue

        # Check indexes are found to be x < xr < xr2
        valid_indices = nums.index(x) < nums.index(xr) < nums.index(xr2)
        if not valid_indices:
            continue

        # Add to triplets
        triplets.append([ x, xr, xr2 ])

    print(triplets)
    return len(triplets)

def test_find_geometric_sequence_triplets():
    assert find_geometric_sequence_triplets([2, 1, 2, 4, 8, 8], 2) == 5
