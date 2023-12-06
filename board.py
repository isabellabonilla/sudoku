from sudoku_generator import generate_sudoku
from cell import Cell
import pygame

class Board:
    def __init__(self, width, height, screen, num_removed):
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard
        self.width = width
        self.height = height
        self.screen = screen
        sudoku_array = generate_sudoku(9,num_removed)
        self.cells = []
        self.editable_cells = []
        for i in range(height): #each row
            cell_row = []
            for j in range(width): #each column
                # append a cell with the same stuff as the sudoku array
                cell_row.append(Cell(sudoku_array[i][j], i, j, self.screen))
                if sudoku_array[i][j] == 0:
                    self.editable_cells.append((i, j)) #append the coordinates of the editable cells
            self.cells.append(cell_row)



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
        # declare cell as selected
        # check each column per row (so check each cell)
        for row in range(self.height): # calls instance variable for length of rows
            for col in range(self.width): # calls instance variable for length of cols
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
        if x <= self.height and y <= self.width:
            return self.cells[x][y]
        '''if a tuple of (x,y) coord is within the displayed board,
        this function returns a tuple of the (row,col) of the cell which was clicked'''
        return None

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves
        for coordinates in self.editable_cells:  # check editable array to find cell
            x, y = coordinates
            if self.cells[x][y].selected: # if selected
                # check OG board, if there is nothin in OG board, remove the sketched value and actual value
                if self.cells[x][y] == 0:
                    self.cells[x][y].sketched_value = 0
                    self.cells[x][y].value = 0


    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.

        for coordinates in self.editable_cells:  # check editable array to find cell
            x, y = coordinates
            if self.cells[x][y].selected:
                self.cells[x][y].set_sketched_value(value)   # uses cell class setter function for setting sketched

    def place_number(self,value):
        # sets the value of the current selected cell equal to user entered value
        #called when the user presses the Enter key IN MAINNNNNN
        for coordinates in self.editable_cells:  # check editable array to find cell
            x, y = coordinates
            if self.cells[y][x].selected(): # if cell is selected and has nothing there but CAN have something there, sketch and set
                if self.cells[x][y] == 0:   # hanges board to cells
                    self.cells[x][y].sketched_value[0]
                    self.cells[x][y].set_cell_value()

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        for coordinates in self.editable_cells:  # check editable array to find cell
            x, y = coordinates
            self.cells[x][y].value = 0
            self.cells[x][y].sketched_value = 0


    def is_full(self):
        for coordinates in self.editable_cells: # check editable array to find cell
            x, y = coordinates
            if self.cells[x][y].value == 0:
                return False
         # if it does not have empty cell --> it is full
        return True

    '''
    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y)
        pass
    '''

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        pass


