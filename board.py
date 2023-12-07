from sudoku_generator import generate_sudoku
from cell import Cell
import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard; this is the returned number
        self.width = width
        self.height = height
        self.num_rows = 9
        self.num_cols = 9
        self.screen = screen
        sudoku_array = generate_sudoku(9, difficulty) #WE MIGHT NOT NEED THIS
        self.cells = []
        self.editable_cells = []
        for i in range(0,self.num_rows): #each row
            cell_row = []
            for j in range(0,self.num_cols): #each column
                # append a cell with the same stuff as the sudoku array
                cell_row.append(Cell(sudoku_array[i][j], i, j, self.screen))
                if sudoku_array[i][j] == 0:
                    self.editable_cells.append((i, j)) #append the coordinates of the editable cells
            self.cells.append(cell_row)
        self.selected_row = 0
        self.selected_col = 0


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

        # Loop through the cells and draw them
        for i in range(0,self.num_rows): #each row
            cell_row = []
            for j in range(0,self.num_cols): #each column
                # append a cell with the same stuff as the sudoku array
                self.cells[i][j].draw()

        # initialize button font
        button_font = pygame.font.Font(None, 40)

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
        reset_rectangle = reset_surface.get_rect(center=(self.width // 4, self.height + 50))
        restart_rectangle = restart_surface.get_rect(center=((self.width // 4) * 2, self.height + 50))
        quit_rectangle = quit_surface.get_rect(center=((self.width // 4) * 3, self.height + 50))

        self.screen.blit(reset_surface, reset_rectangle)
        self.screen.blit(restart_surface, restart_rectangle)
        self.screen.blit(quit_surface, quit_rectangle)
        return (reset_rectangle,restart_rectangle,quit_rectangle)


    def select(self, row, col):
        # marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value
        # declare cell as selected
        # check each column per row (so check each cell)
        #for row in range(self.height): # calls instance variable for length of rows
        #    for col in range(self.width): # calls instance variable for length of cols

        if self.cells[row][col].is_editable():
            # Unselect the currently selected cell
            self.cells[self.selected_row][self.selected_col].selected = False # marked as selected

            # Select the new cell
            self.cells[row][col].selected = True # marked as selected

            # Remember the newly selected cell
            self.selected_row = row
            self.selected_col = col


    def click(self,x,y):
        if x <= self.height and y <= self.width:
            return self.cells[x][y]
        '''if a tuple of (x,y) coord is within the displayed board,
        this function returns a tuple of the (row,col) of the cell which was clicked'''
        return None

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves
        self.cells[self.selected_row][self.selected_col].sketched_value = 0
        self.cells[self.selected_row][self.selected_col].value = 0


    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.

        for coordinates in self.editable_cells:  # check editable array to find cell
            x, y = coordinates
            if self.cells[x][y].selected:
                self.cells[x][y].set_sketched_value(value)   # uses cell class setter function for setting sketched
                self.draw()

    def place_number(self,value):
        # sets the value of the current selected cell equal to user entered value
        #called when the user presses the Enter key IN MAINNNNNN

        if self.cells[self.selected_row][self.selected_col].selected: # if cell is selected and has nothing there but CAN have something there, sketch and set
            self.cells[self.selected_row][self.selected_col].set_cell_value(self.cells[self.selected_row][self.selected_col].sketched_value)


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
    # copied the validity checkers, but adapted to the board class
    def check_row(self, row):
        # each row has no duplicate number
        numbers = []
        for col in range(self.num_cols):
            if self.cells[row][col].value in numbers:
                return False
            else:
                numbers.append(self.cells[row][col].value)

        return True

    def check_col(self, col):
        # each col has no duplicate number
        numbers = []
        for row in range(self.num_rows):
            if self.cells[row][col].value in numbers:
                return False
            else:
                numbers.append(self.cells[row][col].value)

        return True
    def check_box(self, row_start, col_start):
        # determines no duplicate number is contained in the 3x3 box specified on the board
        numbers = []
        for row in range(row_start, row_start + 3): # check the 3*3 rows
            for col in range(col_start, col_start + 3): # check the 3*3 columns
                if self.cells[row][col].value in numbers:
                    return False
                else:
                    numbers.append(self.cells[row][col].value)
        return True

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.
        #checking each row
        for row in range(self.num_rows):
            if not self.check_row(row):
                # if invalid
                return False
        #checking in col
        for col in range(self.num_cols):
            if not self.check_col(col):
                # if invalid
                return False


        #checking each box
        for row_start in range(0, self.num_rows, 3):
            for col_start in range (0, self.num_cols, 3):
                if not self.check_box(row_start, col_start):
                    return False


        # if we made it through all the checks
        return True


