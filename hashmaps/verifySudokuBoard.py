from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    """Verifies whether an incomplete sudoku board is valid (not solvable)"""

    column_hashset = [ set() for _ in range(len(board)) ]
    row_hashset = [ set() for _ in range(len(board)) ]
    subgrid_hashset = [ [ set() for _ in range(len(board) // 3) ] for _ in range(len(board) // 3) ]

    for r in range(len(board)):
        for c in range(len(board[r])): 
            cell_value = board[r][c]

            if cell_value == 0:
                # 0 == empty
                continue

            if cell_value in column_hashset[c]:
                return False
            if cell_value in row_hashset[r]:
                return False
            if cell_value in subgrid_hashset[r // 3][c // 3]:
                return False

            column_hashset[c].add(cell_value)
            row_hashset[r].add(cell_value)
            subgrid_hashset[r // 3][c // 3].add(cell_value)

    return True

def test_main():
    assert verify_sudoku_board([[3,0,6,0,5,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]) == False
