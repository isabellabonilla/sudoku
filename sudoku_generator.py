import math
import random
import pygame, sys


class SudokuGenerator:

    def __init__(self, removed_cells, row_length=9):
        # creating a sudoku board with a 2d list of empty values (0s)
        # initializing class variables

        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = math.sqrt(row_length)

    def get_board(self):
        # returns a 2D python list of numbers, representing the sudoku board

        return self.board

    def print_board(self):
        # displays the board to the console

        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        # determines if num is contained in the specified row of the board
        # if num is already in the specified row, return False

        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False

        return True

    def valid_in_col(self, col, num):
        # determines if num is contained in the specified column of the board
        # if num is already in the specified col, return False

        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False

        return True

    def valid_in_box(self, row_start, col_start, num):
        # determines if num is contained in the 3x3 box specified on the board
        # if num is in the specified box starting at(row_start, col_start), return False.

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False

        return True

    def is_valid(self, row, col, num):
        # determines if it is valid to enter num at (row, col) in the board
        # this is done by checking that num is unused in the appropriate, row, column, and box

        row_start = row - (row % 3)
        col_start = col - (col % 3)
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row_start, col_start, num):
            return True

        return False

    def fill_box(self, row_start, col_start):
        # fills the specified 3x3 box with values
        # for each position, generates a random digit which has not yet been used in the box

        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(digits)

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                while not self.is_valid(row, col, digits[-1]):
                    random.shuffle(digits)

                self.board[row][col] = digits.pop()
                random.shuffle(digits)

    def fill_diagonal(self):
        # fills the three boxes along the main diagonal of the board
        # these are the boxes which start at (0,0), (3,3), and (6,6)
        pass

    def fill_remaining(self, row, col):
        # fills the remaining cells of the board

        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        # constructs a solution by calling fill_diagonal and fill_remaining

        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        pass

def generate_sudoku(size, removed):
    # given a number of rows and number of cells to remove
    # a SudokuGenerator object is created and fills its values, saving as the solved state
    # removes the appropriate number of cells
    # returns the representative 2D Python Lists of the board and solution

    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board