import random
import time
from typing import List

testset = random.sample(range(50000), 10000)

def find_longest_consecutive_chain_brute_force(nums: List[int]) -> int:
    if not nums:
        return 0

    longest_chain = 0

    for startingNumber in nums:
        current_chain = 1
        current_num = startingNumber

        while (current_num + 1) in nums:
            current_chain += 1
            current_num += 1

        longest_chain = max(longest_chain, current_chain)

    return longest_chain

def find_longest_consecutive_chain(nums: List[int]) -> int:
    if not nums:
        return 0

    longest_chain = 0
    nums_hashset = set(nums)

    for startingNumber in nums:
        # Do not search for numbers not at the start of a chain
        if (startingNumber - 1) in nums_hashset:
            continue

        current_chain = 1
        current_num = startingNumber

        while (current_num + 1) in nums_hashset:
            current_chain += 1
            current_num += 1

        longest_chain = max(longest_chain, current_chain)

    return longest_chain

def test_find_longest_consecutive_chain():
    assert find_longest_consecutive_chain([1, 6, 2, 5, 8, 7, 10, 3]) == 4

if __name__ == "__main__":
    print("Brute force approach")

    start = time.perf_counter()

    find_longest_consecutive_chain_brute_force(testset)

    elapsed = time.perf_counter() - start

    print(f"find_longest_consecutive_chain_brute_force took {elapsed:.8f} seconds") 

    print("Hashset approach")

    start = time.perf_counter()

    find_longest_consecutive_chain(testset)

    elapsed = time.perf_counter() - start

    print(f"find_longest_consecutive_chain took {elapsed:.8f} seconds") 
