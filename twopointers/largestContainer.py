from typing import List

def main(heights: List[int]) -> int:
    left = 0
    maxVolume = 0
    right = len(heights) - 1

    while (left < right):
        volume = min(heights[left], heights[right]) * abs(right - left)
        maxVolume = max(maxVolume, volume)

        if (heights[left] < heights[right]):
            left += 1
        elif (heights[right] < heights[left]):
            right -= 1
        else:
            left += 1
            right -= 1

    return maxVolume

def test_main():
    assert(main([])) == 0
    assert(main([1])) == 0
    assert(main([0, 1, 0])) == 0
    assert(main([3, 3, 3, 3])) == 9
    assert(main([1, 2, 3])) == 2
    assert(main([3, 2, 1])) == 2
    assert(main([2, 7, 8, 3, 7, 6])) == 24
    assert(main([2,3,4,5,18,17,6,2,4,8,1])) == 40
