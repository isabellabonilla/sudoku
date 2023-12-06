import sudoku_generator
import cell
import pygame, sys

class Board: # represents an entire Sudoku board, Board object has 81 cell objects
    board_width = 9 #placeholders
    board_height = 9 #placeholders
    def __init__(self, width, height, screen, difficulty):
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard
        self.difficulty = difficulty
            if diff == easy:
                randnum fill --> 31 cells; for i len(arr): count +=1 until count = 31
                generat
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None #fixme
        self.cells81 = []# make array of the row and column numbers that can be editted later
        #we want to make the backend --> boost outward visual --> selected cells

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
        """
        # marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value
        """
        # pygame.Rect and collidepoint() --> see if mouse is on board
        # compute the row and column of the mouse pointer


        pos =  pygame.mouse.get_pos() # get mouse position

        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                row, col = event #idk about the mx,my=event line yet

        if self.rect.collidepoint(x,y):

            row = ? #fixme LATER
            col = ?
            selected_cell = current_cell.(#,row,col,screen) #FIXME tryna call the cell function to assign it to exist?
            return selected_cell

    def click(self,x,y):
        if x <= screen_width/9 and y <= screen_height/10: #FIXME if cell is in the screen size(?)
            self.selected_cell = (int(x),int(y)) # tuple of the row,col of the cell clicked

        else:
            return None

    def clear(self):

        row, col = self.selected_cell
        if cell[row][col]



        #clears the value cell, note that the user can only remove the cell values and sketched value that filled by themselves
        # basically, auto gen cells cant be cleared?

    def sketch(self,value):
        #sets the sketched value of the current selected cell equal to user entered value
        # it will be displayed at the top left corner of the cell using the draw() function

    def place_number(self,value):
        # sets the value of the current selected cell equal to user entered value
        #called when the user presses the Enter key

    def reset_to_original(self):
        #resets all cells in the board to their original values (0 = cleared, otherwise --> corresp digit)

    def is_full(self):
        #returns a boolean value indicating whether the board is full or not

    def update_board(self):
        #updates the underlying 2d board with the values in all cells

    def find_empty(self):
        #fins empty cell and returns its row and col as a tuple (x,y)

    def check_board(self):
        #check whether the sudoku board is solved correctly


