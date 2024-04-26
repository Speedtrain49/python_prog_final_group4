from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
import pygame
import sys

textColor = "black"
width = 500
height = 600
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

    pygame.display.flip()

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
    while True:
        pass


if __name__ == "__main__":
    main()