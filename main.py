from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
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
                        print("easy selected")
                        play(screen, 30)
                    elif mediumRect.collidepoint(event.pos):
                        print("medium selected")
                        play(screen, 40)
                    elif hardRect.collidepoint(event.pos):
                        print("hard selected")
                        play(screen, 50)
        pygame.display.flip()


def play(screen, mode):
    font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 30)
    smaller_font = pygame.font.Font(None, 25)
    large_font = pygame.font.Font(None, 60)

    button_1_rect = pygame.Rect(0, height - 60, 180, 60)
    button_2_rect = pygame.Rect(180, height - 60, 180, 60)
    button_3_rect = pygame.Rect(360, height - 60, 180, 60)
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

    while running:

        pygame.display.flip()

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                print("Quit")
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_over_button(mouse_pos, button_1_rect):
                    # Reset board to initial state
                    print("Reset")
                elif is_over_button(mouse_pos, button_2_rect):
                    # Restart will take the user back to the welcome screen
                    print("Restart")
                    draw_game_start(screen)
                elif is_over_button(mouse_pos, button_3_rect):
                    # Exit will end the game
                    print("Quit")
                    running = False
                    pygame.quit()
                    sys.exit()
def main():

    #EVERYTHING HERE IS FOR TESTING
    # print(p.board)
    # SudokuGenerator.is_valid(p, 1, 1, 9)
    # p.fill_diagonal()
    # p.print_board()
    # print(" ")
    # p.fill_remaining(0, 0)
    # p.print_board()
    # print(" ")
    # p.remove_cells()
    # p.print_board()


    #Need to prompt user for gamemode easy medium or hard
    #in the call below I am passing in 50 for a hard game

    #I modified generate_sudoku to return the board (b) and the solution to the board (a)
    b, a = generate_sudoku(9, 50)
    print(b)
    print(a)

    #Initialises pygame
    pygame.init()
    screen = pygame.display.set_mode((width,height))

    draw_game_start(screen)



if __name__ == "__main__":
    main()