from typing import List

test = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]

def track_zeroes_in_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
        Returns a new matrix with all rows and columns set to 0 where the original matrix had a 0
        in the respective row or column.

        1. Set two flags to indicate if there are 0s in the first column and row
        2. Traverse the submatrix for 0s, setting corresponding column and row indices to 0 as a marker
        3. Using the markers set in step #2, iterate over the submatrix setting any cell corresponding
            to a marker to 0
        4. If a column or row flag is true, set all the cells in the column or row to 0s
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    first_column_has_zero = False
    first_row_has_zero = 0 in matrix[0]
    matrix_zeroed = [row[:] for row in matrix] 

    # Check if any of column 0's cells are equal to 0
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_column_has_zero = True
            break
    
    # Traverse submatrix looking for 0s to mark the first column and row
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[r])):
            if matrix[r][c] == 0:
                matrix_zeroed[r][0] = 0
                matrix_zeroed[0][c] = 0

    # Traverse the submatrix setting all cells to 0 if it's marker row or column is 0
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[r])):
            if matrix_zeroed[0][c] == 0 or matrix_zeroed[r][0] == 0:
                matrix_zeroed[r][c] = 0

    if first_row_has_zero:
        for c in range(len(matrix_zeroed[0])):
            matrix_zeroed[0][c] = 0

    if first_column_has_zero:
        for row in matrix_zeroed:
           row[0] = 0

    for row in matrix:
        print(row)

    for row in matrix_zeroed:
        print(row)

    return matrix_zeroed

def test_main():
    assert track_zeroes_in_matrix(test) == [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
    assert track_zeroes_in_matrix([]) == []
    assert track_zeroes_in_matrix([[]]) == [[]]

if __name__ == "__main__":
    track_zeroes_in_matrix(test)

