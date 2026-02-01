from collections import defaultdict
from typing import List

def find_geometric_sequence_triplets(
    nums: List[int],
    ratio: int
) -> int:
    """
        Finds a sequence of geometric triplets in a list of integers.

        A sequence of geometric triplets is equivalent of 3 numbers in a row which:
        1. Values are equivalent to x, xr, xr^2
        2. Indices of each value in the list are x < xr < xr^2
    """

    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0

    # Store the frequency of each number in our right map
    for num in nums:
        right_map[num] += 1

    # Search for triplets (num represents the middle value)
    for num in nums:
        # Decrease the frequency of num in the right_map since num represents the new current middle
        right_map[num] -= 1

        if num % ratio == 0:
           count += left_map[num // ratio] * right_map[num * ratio]

        # Increase the frequency of num in the left_map since it will no longer be the current middle
        left_map[num] += 1

    return count

def test_find_geometric_sequence_triplets():
    assert find_geometric_sequence_triplets([2, 1, 2, 4, 8, 8], 2) == 5
