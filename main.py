from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from board import Board
import pygame
import sys

textColor = "black"
width = 500
height = 600



#used to determine whether mouse is over button
def is_over_button(pos, button_rect):
    x, y = pos
    if button_rect.left < x < button_rect.right and button_rect.top < y < button_rect.bottom:
        return True
    return False

def draw_game_start(screen):
    #sets font sizes
    titleFont = pygame.font.Font(None,70)
    subFont = pygame.font.Font(None,50)

    #sets colors
    screen.fill(color="white")
    boxColors = "orange"

    #draws title text
    titleText = titleFont.render("Welcome to Sudoku",0,textColor)
    titleRect = titleText.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(titleText, titleRect)

    #draws button text
    optionText = subFont.render("Select Game Mode:",0,textColor)
    optionRect = optionText.get_rect(center=(width // 2, height // 2))
    screen.blit(optionText, optionRect)

    #draws Options
    #draws easy box
    easyBackG = pygame.Rect(10, 360, 160,80)
    easyText = subFont.render("Easy",0,textColor)
    easySurface = pygame.Surface((easyText.get_size()[0] + 20, easyText.get_size()[1] + 20))
    easySurface.fill(color="white")
    easySurface.blit(easyText,(10,10))
    easyRect = easySurface.get_rect(center=(width // 2 - 160, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, easyBackG)
    screen.blit(easySurface,easyRect)

    #draws medium box
    mediumBackG = pygame.Rect(170, 360, 160, 80)
    mediumText = subFont.render("Medium", 0, textColor)
    mediumSurface = pygame.Surface((mediumText.get_size()[0] + 20, mediumText.get_size()[1] + 20))
    mediumSurface.fill(color="white")
    mediumSurface.blit(mediumText, (10, 10))
    mediumRect = mediumSurface.get_rect(center=(width // 2 , height // 2 + 100))
    pygame.draw.rect(screen, boxColors, mediumBackG)
    screen.blit(mediumSurface, mediumRect)

    #draws hard box
    hardBackG = pygame.Rect(330, 360, 160, 80)
    hardText = subFont.render("Hard", 0, textColor)
    hardSurface = pygame.Surface((hardText.get_size()[0] + 20, hardText.get_size()[1] + 20))
    hardSurface.fill(color="white")
    hardSurface.blit(hardText, (10, 10))
    hardRect = hardSurface.get_rect(center=(width // 2 + 160, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, hardBackG)
    screen.blit(hardSurface, hardRect)

    #Traps user until they select a difficulty or close the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #This is how we select difficulties,
                    #replace the print with the code to draw board and such, then go back to main.
                    if easyRect.collidepoint(event.pos):
                        if play(screen, 30) == 1:
                            win_screen(screen)
                        else:
                            loose_screen(screen)
                    elif mediumRect.collidepoint(event.pos):
                        if play(screen, 40) == 1:
                            win_screen(screen)
                        else:
                            loose_screen(screen)
                    elif hardRect.collidepoint(event.pos):
                        if play(screen, 50) == 1:
                            win_screen(screen)
                        else:
                            loose_screen(screen)
        pygame.display.flip()

def loose_screen(screen):
    # sets font sizes
    titleFont = pygame.font.Font(None, 70)
    subFont = pygame.font.Font(None, 50)

    # sets colors
    screen.fill(color="white")
    boxColors = "orange"

    # draws title text
    titleText = titleFont.render("Game Over :(", 0, textColor)
    titleRect = titleText.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(titleText, titleRect)

    # draws Option

    # draws medium box
    mediumBackG = pygame.Rect(150, 360, 200, 80)
    mediumText = subFont.render("RESTART", 0, textColor)
    mediumSurface = pygame.Surface((mediumText.get_size()[0] + 20, mediumText.get_size()[1] + 20))
    mediumSurface.fill(color="white")
    mediumSurface.blit(mediumText, (10, 10))
    mediumRect = mediumSurface.get_rect(center=(width // 2, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, mediumBackG)
    screen.blit(mediumSurface, mediumRect)


    # Traps user until they select a difficulty or close the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # This is how we select difficulties,
                    # replace the print with the code to draw board and such, then go back to main.
                    if mediumRect.collidepoint(event.pos):
                        draw_game_start(screen)
        pygame.display.flip()

def win_screen(screen):
    # sets font sizes
    titleFont = pygame.font.Font(None, 70)
    subFont = pygame.font.Font(None, 50)

    # sets colors
    screen.fill(color="white")
    boxColors = "orange"

    # draws title text
    titleText = titleFont.render("Game Won!", 0, textColor)
    titleRect = titleText.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(titleText, titleRect)

    # draws Option

    # draws medium box
    mediumBackG = pygame.Rect(170, 360, 160, 80)
    mediumText = subFont.render("EXIT", 0, textColor)
    mediumSurface = pygame.Surface((mediumText.get_size()[0] + 20, mediumText.get_size()[1] + 20))
    mediumSurface.fill(color="white")
    mediumSurface.blit(mediumText, (10, 10))
    mediumRect = mediumSurface.get_rect(center=(width // 2, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, mediumBackG)
    screen.blit(mediumSurface, mediumRect)


    # Traps user until they select a difficulty or close the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # This is how we select difficulties,
                    # replace the print with the code to draw board and such, then go back to main.
                    if mediumRect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()

def play(screen, mode):

    screen.fill(color="white")

    board_play = Board(width, height, screen, mode)

    font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 30)
    smaller_font = pygame.font.Font(None, 25)
    large_font = pygame.font.Font(None, 60)

    button_1_rect = pygame.Rect(0, height - 100, 180, 110)
    button_2_rect = pygame.Rect(180, height - 100, 180, 110)
    button_3_rect = pygame.Rect(360, height - 100, 180, 110)
    #inititating screen
    running = True

    screen.fill(color="white")
    #draw buttons - for sudoku screen
    pygame.draw.rect(screen, (200, 200, 200), button_1_rect)
    pygame.draw.rect(screen, (200, 200, 200), button_2_rect)
    pygame.draw.rect(screen, (200, 200, 200), button_3_rect)

    # Button labels
    reset_text = small_font.render("Reset", True, (0, 0, 0))
    restart_text = small_font.render("Restart", True, (0, 0, 0))
    exit_text = small_font.render("Exit", True, (0, 0, 0))

    # Buttons for sudoku game
    screen.blit(reset_text, (button_1_rect.centerx - reset_text.get_width() // 2, button_1_rect.centery - reset_text.get_height() // 2))
    screen.blit(restart_text, (button_2_rect.centerx - restart_text.get_width() // 2, button_2_rect.centery - restart_text.get_height() // 2))
    screen.blit(exit_text, (button_3_rect.centerx - exit_text.get_width() // 2, button_3_rect.centery - exit_text.get_height() // 2))

    #checks if mouse on screen
    screen_rect = pygame.Rect(0, 0, width, height)

    board_play.draw()
    col, row = 0, 0
    old_mouse_x, old_mouse_y = 0, 0

    print(board_play.sudoku)
    print(board_play.sudokuans)

    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_over_button(mouse_pos, button_1_rect):
                    # Reset board to initial state
                    board_play.reset_to_original()
                elif is_over_button(mouse_pos, button_2_rect):
                    # Restart will take the user back to the welcome screen
                    draw_game_start(screen)
                elif is_over_button(mouse_pos, button_3_rect):
                    # Exit will end the game
                    pygame.quit()
                    sys.exit()
                    running = False
                elif screen_rect.collidepoint(mouse_pos):
                    #selects square
                    board_play.select(10, 10)
                    col, row = board_play.click(mouse_x, mouse_y)
                    board_play.select(col, row)
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    if event.key == pygame.K_1:
                        board_play.sketch(1,col,row)
                    elif event.key == pygame.K_2:
                        board_play.sketch(2,col,row)
                    elif event.key == pygame.K_3:
                        board_play.sketch(3,col,row)
                    elif event.key == pygame.K_4:
                        board_play.sketch(4,col,row)
                    elif event.key == pygame.K_5:
                        board_play.sketch(5,col,row)
                    elif event.key == pygame.K_6:
                        board_play.sketch(6,col,row)
                    elif event.key == pygame.K_7:
                        board_play.sketch(7,col,row)
                    elif event.key == pygame.K_8:
                        board_play.sketch(8,col,row)
                    elif event.key == pygame.K_9:
                        board_play.sketch(9,col,row)
                elif event.key == pygame.K_BACKSPACE:
                    board_play.clear(col, row)
                elif event.key == pygame.K_RETURN:
                    board_play.place_number(col, row)
                if event.key == pygame.K_UP and row != 1:
                    board_play.select(10, 10)
                    col, row = (col, row - 1)
                    board_play.select(col, row)
                elif event.key == pygame.K_DOWN and row != 9:
                    board_play.select(10, 10)
                    col, row = (col, row + 1)
                    board_play.select(col, row)
                elif event.key == pygame.K_LEFT and col != 1:
                    board_play.select(10, 10)
                    col, row = (col - 1, row)
                    board_play.select(col, row)
                elif event.key == pygame.K_RIGHT and col != 9:
                    board_play.select(10, 10)
                    col, row = (col + 1, row)
                    board_play.select(col, row)
        if board_play.is_full():
            running = False
    if board_play.check_board() == True:
        return 1
    else:
        return 2






def main():

    #Initialises pygame
    while True:
        pygame.init()
        screen = pygame.display.set_mode((width,height))
        draw_game_start(screen)




if __name__ == "__main__":
    main()