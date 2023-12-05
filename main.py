import pygame, sys
pygame.font.init()


def draw_game_start(screen):
    # initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # color background
    screen.fill((255, 255, 255))

    # initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, (0, 176, 188))
    title_rectangle = title_surface.get_rect(center=(400 // 2, 400 // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # initialize buttons
    # initialize text first
    start_text = button_font.render("Start", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # initialize button background color and text
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill((0, 176, 188))
    start_surface.blit(start_text, (10, 10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill((0, 176, 188))
    quit_surface.blit(quit_text, (10, 10))

    # initialize button rectangle
    start_rectangle = start_surface.get_rect(center=(400 // 2, 400 // 2 + 50))
    quit_rectangle = quit_surface.get_rect(center=(400 // 2, 400 // 2 + 150))

    # draw buttons
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    # checks if mouse is on start button
                    return # if mouse is on start button we can return to main
                elif quit_rectangle.collidepoint(event.pos):
                    # if the mouse is on the quit button, exit the game
                    sys.exit()
        pygame.display.update()

screen = pygame.display.set_mode((400, 400))
draw_game_start(screen)