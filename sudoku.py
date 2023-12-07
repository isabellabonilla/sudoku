import pygame
import sys
from board import Board

pygame.init()
pygame.font.init()
width = 900
height = 1000

# random constants in code
screen = pygame.display.set_mode((900, 1000))
board_grid_surface = pygame.Surface((screen.get_width(), (9 * (screen.get_height() // 10))))
board_grid_rectangle = board_grid_surface.get_rect(center=(screen.get_width() / 2, (9 * screen.get_height() // 10) / 2))


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
                    cells_popped = 30
                    return cells_popped  # if mouse is on easy button we can return option 1 to main
                elif start_medium_rectangle.collidepoint(event.pos):
                    # checks if mouse is on medium button
                    cells_popped = 40
                    return cells_popped  # if mouse is on medium button we can return option 2 to main
                elif start_hard_rectangle.collidepoint(event.pos):
                    # checks if mouse is on hard button
                    cells_popped = 50
                    return cells_popped  # if mouse is on hard button we can return option 3 to main
                elif quit_rectangle.collidepoint(event.pos):
                    # if the mouse is on the quit button, exit the game
                    sys.exit()
                    # or return something like 0 and have main decide what to do with it in a loop
        pygame.display.update()


def game_over(screen, win):
    # game over font
    game_over_font = pygame.font.Font(None, 100)
    end_button_font = pygame.font.Font(None, 70)
    screen.fill((255, 255, 255))

    # if you win, you can only quit the game
    # if you lose, you can only restart
    if win:
        text = 'Game Won!'
        button_text = 'Quit'
    else:
        text = "Game Over :("
        button_text = 'Restart'

    # initializes game over button
    game_over_text = game_over_font.render(text, 0, (255, 255, 255))
    game_over_surface = pygame.Surface((game_over_text.get_size()[0] + 20, game_over_text.get_size()[1] + 20))
    game_over_surface.fill((0, 176, 188))
    game_over_rectangle = game_over_surface.get_rect(center=(width // 2, height // 2 - 100))
    game_over_surface.blit(game_over_text, (10, 10))

    end_button_text = end_button_font.render(button_text, 0, (255, 255, 255))
    end_button_surface = pygame.Surface((end_button_text.get_size()[0] + 20, end_button_text.get_size()[1] + 20))
    end_button_surface.fill((0, 176, 188))
    end_button_rectangle = end_button_surface.get_rect(center=(width // 2, height // 2 + 100))
    end_button_surface.blit(end_button_text, (10, 10))

    # displays game over button on interface
    screen.blit(game_over_surface, game_over_rectangle)
    screen.blit(end_button_surface, end_button_rectangle)

    # if you quit, the system is exited
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_button_rectangle.collidepoint(event.pos):
                    if win:
                        sys.exit()
                    else:
                        return
        pygame.display.update()


def bottom_buttons():
    # initialize buttons
    # initialize text first
    button_font = pygame.font.Font(None, 70)
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
    reset_rectangle = reset_surface.get_rect(center=(width // 4, 9 * height // 10))
    restart_rectangle = restart_surface.get_rect(center=((width // 4) * 2, 9 * height // 10))
    quit_rectangle = quit_surface.get_rect(center=((width // 4) * 3, 9 * height // 10))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    return reset_rectangle, restart_rectangle, quit_rectangle


difficulty = draw_game_start(screen)


def main():
    # initialize button font
    global sketched_value
    button_font = pygame.font.Font(None, 20)
    height = 1000
    width = 900
    screen_width = width
    screen_height = height

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

    start_easy_rectangle = start_easy_surface.get_rect(center=(screen_width // 4, screen_height // 2 + 50))
    start_medium_rectangle = start_medium_surface.get_rect(center=((screen_width // 4) * 2, screen_height // 2 + 50))
    start_hard_rectangle = start_hard_surface.get_rect(center=((screen_width // 4) * 3, screen_height // 2 + 50))
    quit_rectangle = quit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 150))

    # define difficulty as game start with screen as parameter
    # then sudoku board with the key size 9 and difficulty selected

    clicked = None
    game_set_over = False
    win = 0
    difficulty = draw_game_start(screen)

    ############## END OF START SCREEN CODE*************************

    current_game = Board(900, 900, screen, difficulty)

    reset_rectangle, restart_rectangle, quit_rectangle = current_game.draw()

    while True:
        current_game.draw()
        # after current game is made, print the board and overwrite the start screen visual
        pygame.display.update()
        # While in the game check for the bottom buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not game_set_over:
                if reset_rectangle.collidepoint(event.pos):
                    current_game.reset_to_original()
                if restart_rectangle.collidepoint(event.pos):
                    difficulty = draw_game_start(screen)
                    current_game = Board(900, 900, screen, difficulty)  # add sudoku_board[0] if issues :)
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
                if board_grid_rectangle.collidepoint(event.pos):
                    current_cell_row = event.pos[1] // 100
                    current_cell_col = event.pos[0] // 100
                    current_game.select(current_cell_row, current_cell_col)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:  # listens for key press event and if that happens, accept 1-9 values
                if pygame.K_1 <= event.key <= pygame.K_9:  # accepts range 1-9 inclusive
                    sketched_value = event.key - 48
                    current_game.sketch(sketched_value)

                elif event.key == pygame.K_RETURN:
                    current_game.place_number(sketched_value)

                    if current_game.is_full():
                        game_over(screen, current_game.check_board())
                        difficulty = draw_game_start(screen)
                        current_game = Board(900, 900, screen, difficulty)  # add sudoku_board[0] if issues :)

                elif event.key == pygame.K_BACKSPACE:
                    current_game.clear()  # calls method from board to clear the CELL value

                elif event.key == pygame.K_UP:
                    if current_game.selected_row > 0:
                        current_game.select(current_game.selected_row-1, current_game.selected_col)
                elif event.key == pygame.K_DOWN:
                    if current_game.selected_row < 8:
                        current_game.select(current_game.selected_row+1, current_game.selected_col)
                elif event.key == pygame.K_LEFT:
                    if current_game.selected_col > 0:
                        current_game.select(current_game.selected_row, current_game.selected_col-1)
                elif event.key == pygame.K_RIGHT:
                    if current_game.selected_col < 8:
                        current_game.select(current_game.selected_row, current_game.selected_col+1)


if __name__ == '__main__':
    main()
