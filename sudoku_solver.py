# sudoku_solver.py
#
# This program solves a Sudoku puzzle using backtracking
#
# Carina Sylvester

# SUDOKU RULES:
# Consists of a sudoku of 81 squares, divided into 9 boxes, each containing 9 squares.
# Each of the 9 boxes has to contain all the numbers 1-9 within its squares.
# Each number can only appear once in a row, column or box.
# A proper Sudoku only has one correct solution.

# Sudoku retrieved from: https://printablecreative.com/sudoku-generator

sudoku = [
    # Represents the unsolved sudoku
    # 0 = Blank square
    [0,0,0,0,0,0,7,0,0],
    [0,0,0,7,0,0,2,0,0],
    [0,0,7,8,0,4,0,0,0],
    [0,0,0,0,0,0,0,2,0],
    [7,4,0,0,0,0,5,0,6],
    [0,0,0,0,0,0,8,7,0],
    [0,0,4,2,0,6,0,0,0],
    [2,0,5,3,0,0,6,0,0],
    [8,0,0,0,0,0,0,0,0]
]

# Loops through the unsolved sudoku board to find an empty (0) square
# and returns the position of that empty square
def findEmpty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # Returns a tuple denoting the row and column

# Checks whether the number inserted into the empty position is valid
def valid(sudoku, number, position):
    # Checks every number in the row by looping through every single column
    # to make sure it is not equal to the number that was just inserted
    # (ignoring the number that was just inserted)
    for i in range(len(sudoku[0])): 
        if sudoku[position[0]][i] == number and position[1] != i:
            return False

    for i in range(len(sudoku)):
        # Checks every number in the column by looping vertically through single element
        # in the column to make sure it is not equal to the number that was just inserted 
        # (ignoring the number that was just inserted)
        if sudoku[i][position[1]] == number and position[0] != i:
            return False

    # Identifies which box we are currently in
    box_x = position[1] // 3 # -> Box 1 
    box_y = position[0] // 3 # -> Position 0 (highest) 
    # Loops through every element within the box to ensure it is not
    # equal to the number that was just inserted
    for i in range(box_y*3, box_y*3 + 3): # Values will give us either 0,1, or 2
        for j in range(box_x * 3, box_x*3 + 3):
            if sudoku[i][j] == number and (i,j) != position:
                # Invalid
                return False
    # Valid
    return True

# Solves the sudoku by backtracking (recursion), calling the function from inside itself
# Whenever a number proves to be invalid, the function will go back a step and try again
# If we find a valid solution, it'll return true
def solve(sudoku):
    find = findEmpty(sudoku)
    if not find:
        # Solution found
        return True
    else:
        row, column = find
        # Looping through values 1 to 9 to find a valid solution 
    for i in range(1,10): # 1 through 9 inclusively)
        if valid(sudoku, i, (row, column)):
            # Adds the number to sudoku board
            sudoku[row][column] = i
            if solve(sudoku):
                # Solution found
                return True
            # If there are any zeros left, the sudoku isn't solved yet
            sudoku[row][column] = 0
    return False

# Prints the sudoku
def printSudoku(sudoku):
    for i in range(len(sudoku)):
        # Separates the sudoku horizontally into different sections when i is divisible by 3 
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(sudoku[0])):
        # Separates the sudoku vertically into different sections when i is divisible by 3
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")
    return None

def main():
    print("Sudoku:\n")
    printSudoku(sudoku)
    solve(sudoku)
    print("\nSolution:\n")
    printSudoku(sudoku)
    
main()