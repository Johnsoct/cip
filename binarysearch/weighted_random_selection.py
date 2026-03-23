import random
from typing import List

class WeightedRandomSelection:
    def __init__(self, weights: List[int]):
        self.prefix_sums = [ weights[0] ]

        # Implement the "prefix sums pattern"
        for i in range(1, len(weights)):
            # Cumulative addition results in each index being the "endpoint" of each weight
            self.prefix_sums.append(self.prefix_sums[ -1 ] +  weights[ i ])

    def select(self) -> int:
        """Randomly select an item from weights based on weighted randomness"""

        left = 0
        right = len(self.prefix_sums) - 1
        target = random.randint(1, self.prefix_sums[-1])

        while left < right:
            mid = left + (right - left) // 2

            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid

        return left
