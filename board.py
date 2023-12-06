import sudoku_generator
import cell
import pygame, sys

class Board(Cell): # represents an entire Sudoku board, Board object has 81 cell objects

    def __init__(self, width, height, screen, difficulty):
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard
        Cell.__init__(self) #Getting the other variables from class Cell to be accessed in Board
        self.difficulty = difficulty
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        # draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # draws every cell on this board

        self.screen.fill((255, 255, 255))

        # draw grid lines
        for i in range(0, 10):
            # set thickness for lines
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            # draw vertical lines
            pygame.draw.line(self, (0, 0, 0), (i * (self.width // 9), 0),
                             (i * (self.width // 9), self.height), thickness)
            # draw horizontal lines
            pygame.draw.line(self, (0, 0, 0), (0, i * (self.height // 9)),
                             (self.width, i * (self.height // 9)), thickness)

        pass # missing buttons at bottom

    def select(self, row, col):
        i == row
        j == col
        # declare cell as selected
        # check each column per row (so check each cell)
        for i in range(self.board_rows) # calls instance variable for length of rows
            for j in range(self.board_cols) # calls instance variable for length of cols
                self.cells[i][j].selected = True # selects
                



        """
        # marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value
        """
        # pygame.Rect and collidepoint() --> see if mouse is on board
        # compute the row and column of the mouse pointer
        pygame.draw.rect()

        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                row, col = event #idk about the mx,my=event line yet

        if self.board.collidepoint(x,y):
            row = ? #fixme LATER
            col = ?
            selected_cell = current_cell.(#,row,col,screen) #FIXME tryna call the cell function to assign it to exist?
            return selected_cell

    def click(self,x,y):
        if x in Board.width and y in Board.height: #FIXME it should be in the tuple is in the screen
            return cell.(x,y)
        '''if a tuple of (x,y) coord is within the displayed board,
        this function returns a tuple of the (row,col) of the cell which was clicked'''
        return None

    def clear(self):

        #compare cell value with the orginal in board, if not same, delete.
        if cell[row][col] != orignal_board[row][col]:
            del cell[row][col] # or like set it back to the original cell



        #clears the value cell, note that the user can only remove the cell values and sketched value that filled by themselves
        # basically, auto gen cells cant be cleared?

    def sketch(self,value):
        #sets the sketched value of the current selected cell equal to user entered value
        # it will be displayed at the top left corner of the cell using the draw() function

    def place_number(self,value):
        # sets the value of the current selected cell equal to user entered value
        #called when the user presses the Enter key
        for row in range(self.board_rows)
            for col in range(self.board_cols):
                if self.cells[col][row].selected()
                    if self.board[col][row] = 0:
                        self.cells[col][row].sketched_value 0:
                        self.cells[col][row]set_cell_value():

    def reset_to_original(self):
        #resets all cells in the board to their original values (0 = cleared, otherwise --> corresp digit)

    def is_full(self):
        #returns a boolean value indicating whether the board is full or not

    def update_board(self):
        #updates the underlying 2d board with the values in all cells

    def find_empty(self):
        #fins empty cell and returns its row and col as a tuple (x,y)

    def check_board(self):
        #check whether the sudoku board is colved correctly


