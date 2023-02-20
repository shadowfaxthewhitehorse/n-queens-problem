from typing import List

def solve_n_queens(n: int) -> List[List[int]]:
    board = [[False] * n for _ in range(n)]
    solutions = []
    solve_n_queens_helper(board, 0, solutions)
    return solutions

def solve_n_queens_helper(board: List[List[bool]], col: int, solutions: List[List[int]]):
    # Base case: all queens have been placed
    if col == len(board):
        positions = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]:
                    positions.append((i, j))
        solutions.append(positions)
        return
    
    # Try placing a queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            solve_n_queens_helper(board, col + 1, solutions)
            board[row][col] = False

def is_safe(board: List[List[bool]], row: int, col: int) -> bool:
    # Check the row
    if any(board[row][:col]):
        return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    # Check for knight attacks
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] and (abs(row - i) == 2 and abs(col - j) == 1 or
                                abs(row - i) == 1 and abs(col - j) == 2):
                return False

    # All checks passed, it is safe to place a queen here
    return True

def print_board(board: List[List[bool]]):
    for row in board:
        for cell in row:
            print('Q' if cell else '.', end=' ')
        print()
    print()

# DEVNOTES
#
# 
    
# Test the program with a 4x4 board
solutions = solve_n_queens(4)
for solution in solutions:
    board = [[False] * 4 for _ in range(4)]
    for pos in solution:
        board[pos[0]][pos[1]] = True
    print_board(board)
