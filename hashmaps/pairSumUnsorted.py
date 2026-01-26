from typing import List

def main(nums: List[int], target: int) -> List[int]:
    hash = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash:
            return [ hash[complement], i ]
        else:
            hash[num] = i

    return []



def test_main():
    assert set(main([ -1, 3, 4, 2 ], 3)) == {0, 2}
 
