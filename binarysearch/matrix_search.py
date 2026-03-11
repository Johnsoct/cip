from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Search a sorted matrix for the target value and return true if the target exists within the matrix"""

    m = len(matrix) # Length of matrix
    n = len(matrix[0]) # Length of a row
    left = 0
    right = (m * n) - 1

    while left <= right:
        mid = left + (right - left) // 2
        c = mid % n
        r = mid // n

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def test():
    matrix = [
        [ 2, 3, 4, 6 ],
        [ 7, 10, 11, 17 ],
        [ 20, 21, 24, 33 ],
    ]
    assert search_matrix(matrix, 21) == True
