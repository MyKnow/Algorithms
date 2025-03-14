import sys

# [def(x: int, y: int, value: int)] isValid
#
# - Parameter
# : Function that Returns True if "value" can be inserted in (x, y) coordinates based on row, column, and 3x3 sub-grid constraints
# [int] x: An Integer that points to "x coordinates" on the board
# [int] y: An Integer that points to "y coordinates" on the board
# [int] value: An Integer to check if it can be inserted in (x, y) without violating Sudoku rules
#
# - Return
# [bool]: If "value" can be inserted at (x, y) point, return True; if not, return False.
def isValid(x: int, y: int, value: int):
    # Check row and column constraints
    if row_check[y][value] or col_check[x][value] or box_check[(y // 3) * 3 + (x // 3)][value]:
        return False
    return True

# [def(count: int)] solve
#
# - Parameter
# : Function that solves the Sudoku board using Backtracking
# [int] count: An Integer that tracks the index of blankList being processed
#
# - Return
# None: Updates board in place and prints the solution if completed
def solve(count: int):
    # Exit and print board when all blanks are filled
    if count == len(blankList):
        for row in board:
            print(" ".join(map(str, row)))
        sys.exit()
    
    # [int] y, x
    # : Integer pair representing (y, x) coordinates of the blank cell at current index
    y, x = blankList[count]
    
    # Iterate 1 through 9 to find valid values for (x, y)
    for value in range(1, 10):
        if isValid(x, y, value):
            # Mark value as used in row, column, and sub-grid
            row_check[y][value] = col_check[x][value] = box_check[(y // 3) * 3 + (x // 3)][value] = True
            board[y][x] = value
            
            # Recursive DFS call
            solve(count + 1)
            
            # Backtracking: Restore board and unmark value
            board[y][x] = 0
            row_check[y][value] = col_check[x][value] = box_check[(y // 3) * 3 + (x // 3)][value] = False

# [def() -> list(tuple(int, int))] getBlankList
#
# - Returns
# [list(tuple(int, int))] blankList: List of (y, x) coordinates for all empty spaces (value == 0) in the board
def getBlankList():
    return [(y, x) for y in range(9) for x in range(9) if board[y][x] == 0]

# Initialize Sudoku board with input values
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# Initialize tracking arrays for row, column, and sub-grid constraints
row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

# Populate constraint tracking arrays with initial board values
for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
            value = board[y][x]
            row_check[y][value] = col_check[x][value] = box_check[(y // 3) * 3 + (x // 3)][value] = True

# Get list of empty cells
blankList = getBlankList()

# Start solving the Sudoku puzzle
solve(0)