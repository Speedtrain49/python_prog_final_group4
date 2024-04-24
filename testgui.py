"""
all this does is create a sudoku grid with three buttons at the bottom
can select cell that you want to change and it will outline it in red
once a cell is selected you can press a number to change it.
Run this code by itself to test it out

This is just a testing program, and parts of it need to be taken and used in the Board and Cell
classes and eventually all formatted into main.py for the final submission.
"""


import pygame
import random

#initializes Pygame
pygame.init()

#set up the screen dimensions
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500
CELL_SIZE = 50
GRID_SIZE = 9

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
# BLUE = (0, 0, 255)

#sets up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

#loads fonts
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

#define the function to draw the grid for sudoku
def draw():
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT), 3)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), 3)
        else:
            pygame.draw.line(screen, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT))
            pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE))

#this puts the spots on the grid where the numbers from the 2d list go
def generate_sudoku():
   #use board (b) from main.py logic here

    #Simple puzzle I created as an example
    puzzle = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            puzzle[i][j] = (i + j) % GRID_SIZE + 1
    return puzzle

#define the function to draw the Sudoku puzzle on the grid (this stays the same)
def draw_puzzle(puzzle):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if puzzle[i][j] != 0:
                text_surface = font.render(str(puzzle[i][j]), True, BLACK)
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)

#define the function to draw the selected cell (outlines the selected cell in red)
def draw_selected_cell(selected_row, selected_col):
    pygame.draw.rect(screen, RED, (selected_col * CELL_SIZE, selected_row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

#function that validates the board
def check_board(board):
    #returns true or false
    return True

#function to get the cell position from mouse coordinates
def get_cell_pos(mouse_pos):
    row = mouse_pos[1] // CELL_SIZE
    col = mouse_pos[0] // CELL_SIZE
    return row, col

#function to check if mouse is over a button
def is_over_button(pos, button_rect):
    x, y = pos
    if button_rect.left < x < button_rect.right and button_rect.top < y < button_rect.bottom:
        return True
    return False

#main function
def main():
    puzzle = generate_sudoku()
    selected_row, selected_col = 0, 0

    #button dimensions and positions
    button_width = 150
    button_height = 50
    reset_button_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, button_width, button_height)
    restart_button_rect = pygame.Rect(150, SCREEN_HEIGHT - 50, button_width, button_height)
    exit_button_rect = pygame.Rect(300, SCREEN_HEIGHT - 50, button_width, button_height)

    #game loop
    running = True
    while running:
        screen.fill(WHITE)
        draw()
        draw_puzzle(puzzle)
        draw_selected_cell(selected_row, selected_col)

        #draw buttons
        pygame.draw.rect(screen, GRAY, reset_button_rect)
        pygame.draw.rect(screen, GRAY, restart_button_rect)
        pygame.draw.rect(screen, GRAY, exit_button_rect)

        #button labels
        reset_text = small_font.render("Reset", True, BLACK)
        restart_text = small_font.render("Restart", True, BLACK)
        exit_text = small_font.render("Exit", True, BLACK)

        screen.blit(reset_text, (reset_button_rect.centerx - reset_text.get_width() // 2, reset_button_rect.centery - reset_text.get_height() // 2))
        screen.blit(restart_text, (restart_button_rect.centerx - restart_text.get_width() // 2, restart_button_rect.centery - restart_text.get_height() // 2))
        screen.blit(exit_text, (exit_button_rect.centerx - exit_text.get_width() // 2, exit_button_rect.centery - exit_text.get_height() // 2))

        pygame.display.flip()

        #event handling
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == 1024:
                print(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_over_button(mouse_pos, reset_button_rect):
                    #resets puzzle
                    #dsplay the original board with removed cells depending on gamemode(easy medium hard)
                    print("Reset")
                elif is_over_button(mouse_pos, restart_button_rect):
                    #restarts puzzle
                    puzzle = generate_sudoku()
                    selected_row, selected_col = 0, 0
                    print("Restart")
                elif is_over_button(mouse_pos, exit_button_rect):
                    #exits game
                    print("Exit")
                    running = False
                else:
                    selected_row, selected_col = get_cell_pos(mouse_pos)
                    print(selected_row, selected_col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_row = (selected_row - 1) % GRID_SIZE
                elif event.key == pygame.K_DOWN:
                    selected_row = (selected_row + 1) % GRID_SIZE
                elif event.key == pygame.K_LEFT:
                    selected_col = (selected_col - 1) % GRID_SIZE
                elif event.key == pygame.K_RIGHT:
                    selected_col = (selected_col + 1) % GRID_SIZE
                elif event.key == pygame.K_1:
                    puzzle[selected_row][selected_col] = 1
                elif event.key == pygame.K_2:
                    puzzle[selected_row][selected_col] = 2
                elif event.key == pygame.K_3:
                    puzzle[selected_row][selected_col] = 3
                elif event.key == pygame.K_4:
                    puzzle[selected_row][selected_col] = 4
                elif event.key == pygame.K_5:
                    puzzle[selected_row][selected_col] = 5
                elif event.key == pygame.K_6:
                    puzzle[selected_row][selected_col] = 6
                elif event.key == pygame.K_7:
                    puzzle[selected_row][selected_col] = 7
                elif event.key == pygame.K_8:
                    puzzle[selected_row][selected_col] = 8
                elif event.key == pygame.K_9:
                    puzzle[selected_row][selected_col] = 9
                elif event.key == pygame.K_RETURN:
                    if check_board(puzzle):
                        print("Game Won!")
                    else:
                        print("Game Over :(")

    pygame.quit()

if __name__ == "__main__":
    main()