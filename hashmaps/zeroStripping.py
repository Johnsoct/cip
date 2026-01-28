from typing import List

def zero_striping_hashsets(matrix: List[List[int]]) -> List[List[int]]:
    """
        Returns a new matrix with all rows and columns set to 0 where the original matrix had a 0
        in the respective row or column.
    """

    columns_with_zeroes_hashset = set()
    modified_matrix = [ row[:] for row in matrix ]
    rows_with_zeros_hashset = set()

    for ri, r in enumerate(matrix):
        for ci, c in enumerate(r):
            if c == 0:
                columns_with_zeroes_hashset.add(ci)
                rows_with_zeros_hashset.add(ri)

    for ri, r in enumerate(matrix):
        for ci, c in enumerate(r):
            num = matrix[ri][ci]

            if ri in rows_with_zeros_hashset:
                num = 0
            if ci in columns_with_zeroes_hashset:
                num = 0

            modified_matrix[ri][ci] = num

    return modified_matrix

def test_main():
    assert zero_striping_hashsets([[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]) == [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
