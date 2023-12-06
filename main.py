import sys
from board import Board
import sudoku_generator
import pygame
from cell import Cell


pygame.font.init()


def draw_game_start(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # color background
    screen.fill((255, 255, 255))

    # initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, (0, 176, 188))
    title_rectangle = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # initialize buttons
    # initialize text first
    start_easy_text = button_font.render("Easy", 0, (255, 255, 255))
    start_medium_text = button_font.render("Medium", 0, (255, 255, 255))
    start_hard_text = button_font.render("Hard", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # initialize button background color and text
    start_easy_surface = pygame.Surface((start_easy_text.get_size()[0] + 20, start_easy_text.get_size()[1] + 20))
    start_easy_surface.fill((0, 176, 188))
    start_easy_surface.blit(start_easy_text, (10, 10))

    start_medium_surface = pygame.Surface((start_medium_text.get_size()[0] + 20, start_medium_text.get_size()[1] + 20))
    start_medium_surface.fill((0, 176, 188))
    start_medium_surface.blit(start_medium_text, (10, 10))

    start_hard_surface = pygame.Surface((start_hard_text.get_size()[0] + 20, start_hard_text.get_size()[1] + 20))
    start_hard_surface.fill((0, 176, 188))
    start_hard_surface.blit(start_hard_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill((0, 176, 188))
    quit_surface.blit(quit_text, (10, 10))

    # initialize button rectangle
    start_easy_rectangle = start_easy_surface.get_rect(center=(screen_width // 4, screen_height // 2 + 50))
    start_medium_rectangle = start_medium_surface.get_rect(center=((screen_width // 4) * 2, screen_height // 2 + 50))
    start_hard_rectangle = start_hard_surface.get_rect(center=((screen_width // 4) * 3, screen_height // 2 + 50))
    quit_rectangle = quit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 150))

    # draw buttons
    screen.blit(start_easy_surface, start_easy_rectangle)
    screen.blit(start_medium_surface, start_medium_rectangle)
    screen.blit(start_hard_surface, start_hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_easy_rectangle.collidepoint(event.pos):
                    # checks if mouse is on easy button
                    return 30 # if mouse is on easy button we can return option 1 to main
                elif start_medium_rectangle.collidepoint(event.pos):
                    # checks if mouse is on medium button
                    return 40 # if mouse is on medium button we can return option 2 to main
                elif start_hard_rectangle.collidepoint(event.pos):
                    # checks if mouse is on hard button
                    return 50 # if mouse is on hard button we can return option 3 to main
                elif quit_rectangle.collidepoint(event.pos):
                    # if the mouse is on the quit button, exit the game
                    sys.exit()
                    # or return something like 0 and have main decide what to do with it in a loop
        pygame.display.update()





screen = pygame.display.set_mode((900, 1000))
difficulty = draw_game_start(screen)
#original_board = sudoku_generator.generate_sudoku(9, difficulty)
game_board = Board(screen.get_width(), 9 * (screen.get_height()//10), screen, difficulty)

game_board.draw()

# Main Game Play Loop
board_grid_surface = pygame.Surface((screen.get_width(), (9 * (screen.get_height()//10))))
board_grid_rectangle = board_grid_surface.get_rect(center= (screen.get_width()/2,(9 *screen.get_height()//10)/2))

'''for i in range(0, 10):
    test_cell_orig = Cell(i + 1, 0, i, screen)
    if i == 0:
        test_cell_orig.set_selected(True)
        test_cell_orig.draw()
        test_cell_orig.set_selected(False)
    test_cell_orig.draw()
    test_cell_sketch = Cell(0, 1, i, screen)
    test_cell_sketch.set_sketched_value((i + 4) % 9)
    test_cell_sketch.set_selected((i % 3) == 0)
    test_cell_sketch.draw()
    test_cell_value = Cell(0, 2, i, screen)
    test_cell_value.set_cell_value((i + 7) % 9)
    test_cell_value.set_selected((i % 3) == 2)
    test_cell_value.draw()
    '''
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board_grid_rectangle.collidepoint(event.pos):

                pass # event.pos.x / (screen.get_width()/9)
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()


'''def main():
    # when program starts, display the game start screen with difficulties

    game_set_over = False
    win = 0

    pygame.init()
    ## initialize screen like gigi did above screen = pygame. display.set_mode((900, 1000))
            # set caption
    
    # define difficulty as game start with screen as parameter
    # then sudoku board with the key size 9 and difficulty selected


    clicked = None
    sketched = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type != game_over:
                    pass
                    # code for reset, restart, and exit
        # variables with where user clicked row and column wise
        row = int(event.pos[1]/CELL_SIZE)   # grabs position and takes the 1st index which is row #
        col = int(event.pos[0]/ CELL_SIZE)  # grabs position and takes the 0 index which is col #

        # use these in board to show that its selected using select method from Board
        board.select(row, col) # no self
        # sketched using click method from Board

        if event.type == pygame.KEYDOWN:   # listens for key press event and if that happens, accept 1-9 values
            if pygame.K_1 < event.key <= pygame.K-9:   # accepts range 1-9 inclusive
                sketched_value = event.key # - pygame.K_1 + 1   # sets sketch value to the event key to sketch it on the board
                board.sketch(sketched_value)
            if event.key == pygame.K_RETURN:
                if board.is_full(): ## set an option here that if the board is full and the user submits it, check if right or wrong and end game
                    game_over = True
                else: 
                    board(sketched_value) ## it'll no longer be skecthed, actually place it on the board
            if event.key == pygame.K_BACKSPACE:
                board.clear()  # calls method from board to clear the CELL value
            else:
                #return some sort of error that wrong input was inserted
                pass

if __name__ == '__main__':
    main()
'''