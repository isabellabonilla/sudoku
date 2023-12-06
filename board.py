import sudoku_generator
from cell import Cell
import pygame, sys

class Board(Cell):

    def __init__(self, width, height, screen, difficulty):
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard
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
            pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width // 9), 0),
                             (i * (self.width // 9), self.height), thickness)
            # draw horizontal lines
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height // 9)),
                             (self.width, i * (self.height // 9)), thickness)

        # initialize button font
        button_font = pygame.font.Font(None, 20)

        # initialize buttons
        # initialize text first
        reset_text = button_font.render("Reset", 0, (255, 255, 255))
        restart_text = button_font.render("Restart", 0, (255, 255, 255))
        quit_text = button_font.render("Quit", 0, (255, 255, 255))

        # initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill((0, 176, 188))
        reset_surface.blit(reset_text, (10, 10))

        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill((0, 176, 188))
        restart_surface.blit(restart_text, (10, 10))

        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        quit_surface.fill((0, 176, 188))
        quit_surface.blit(quit_text, (10, 10))

        # initialize button rectangle
        reset_rectangle = reset_surface.get_rect(center=(self.width // 4, 9 * self.height // 10))
        restart_rectangle = restart_surface.get_rect(center=((self.width // 4) * 2, 9 * self.height // 10))
        quit_rectangle = quit_surface.get_rect(center=((self._width // 4) * 3, 9 * self.height // 10))

        self.screen.blit(reset_surface, reset_rectangle)
        self.screen.blit(restart_surface, restart_rectangle)
        self.screen.blit(quit_surface, quit_rectangle)
        pass

    def select(self, row, col):
        # marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value
        
        i == row
        j == col
        # declare cell as selected
        # check each column per row (so check each cell)

        for row in range(self.board_rows) # calls instance variable for length of rows
            for col in range(self.board_cols) # calls instance variable for length of cols
                self.cells[row][col].selected = True # marked as selected

        # pygame.Rect and collidepoint() --> see if mouse is on board
        # compute the row and column of the mouse pointer

        # karla edits
        # pygame.draw.rect()

        # for event in pygame.event.get():
        #     if event.type ==pygame.MOUSEBUTTONDOWN:
        #         row, col = event #idk about the mx,my=event line yet

        # if self.board.collidepoint(x,y):
        #     row = ? #fixme LATER
        #     col = ?
        #     selected_cell = current_cell.(#,row,col,screen) #FIXME tryna call the cell function to assign it to exist?
        #     return selected_cell

    def click(self,x,y):
        if x in Board.width and y in Board.height: #FIXME it should be in the tuple is in the screen
            return cell.(x,y)
        '''if a tuple of (x,y) coord is within the displayed board,
        this function returns a tuple of the (row,col) of the cell which was clicked'''
        return None

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves
        pass

    def sketch(selfself, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        pass

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
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y)
        pass

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        pass



