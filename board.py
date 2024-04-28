import pygame
import sys
from sudoku_generator import generate_sudoku
import random


# Define constants
textColor = "black"
sketchColor = (200, 200, 200)
boldTextColor = (0, 0, 0)
width = 500
height = 600
board_size = 9
cell_size = 50
board_width = board_height = board_size * cell_size
board_x = (width - board_width) // 2
board_y = (height - board_height) // 2
selected_cell = (0, 0)  # Initially select the top-left cell
numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


# Define original_board and cell_status outside of the functions
original_board = None
cell_status = None


# Function to check if the mouse is over a button
def is_over_button(pos, button_rect):
   x, y = pos
   if button_rect.left < x < button_rect.right and button_rect.top < y < button_rect.bottom:
       return True
   return False


# Function to draw the game start screen
def draw_game_start(screen):
    titleFont = pygame.font.Font(None, 70)
    subFont = pygame.font.Font(None, 50)

    screen.fill(color="white")
    boxColors = "orange"

    titleText = titleFont.render("Welcome to Sudoku", 0, textColor)
    titleRect = titleText.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(titleText, titleRect)

    optionText = subFont.render("Select Game Mode:", 0, textColor)
    optionRect = optionText.get_rect(center=(width // 2, height // 2))
    screen.blit(optionText, optionRect)

    easyBackG = pygame.Rect(10, 360, 160, 80)
    easyText = subFont.render("Easy", 0, textColor)
    easySurface = pygame.Surface((easyText.get_size()[0] + 20, easyText.get_size()[1] + 20))
    easySurface.fill(color="white")
    easySurface.blit(easyText, (10, 10))
    easyRect = easySurface.get_rect(center=(width // 2 - 160, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, easyBackG)
    screen.blit(easySurface, easyRect)

    mediumBackG = pygame.Rect(170, 360, 160, 80)
    mediumText = subFont.render("Medium", 0, textColor)
    mediumSurface = pygame.Surface((mediumText.get_size()[0] + 20, mediumText.get_size()[1] + 20))
    mediumSurface.fill(color="white")
    mediumSurface.blit(mediumText, (10, 10))
    mediumRect = mediumSurface.get_rect(center=(width // 2, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, mediumBackG)
    screen.blit(mediumSurface, mediumRect)

    hardBackG = pygame.Rect(330, 360, 160, 80)
    hardText = subFont.render("Hard", 0, textColor)
    hardSurface = pygame.Surface((hardText.get_size()[0] + 20, hardText.get_size()[1] + 20))
    hardSurface.fill(color="white")
    hardSurface.blit(hardText, (10, 10))
    hardRect = hardSurface.get_rect(center=(width // 2 + 160, height // 2 + 100))
    pygame.draw.rect(screen, boxColors, hardBackG)
    screen.blit(hardSurface, hardRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if the left mouse button was pressed
                    if easyRect.collidepoint(event.pos):
                        print("easy selected")
                        return 3  # Return the mode for easy difficulty
                    elif mediumRect.collidepoint(event.pos):
                        print("medium selected")
                        return 40  # Return the mode for medium difficulty
                    elif hardRect.collidepoint(event.pos):
                        print("hard selected")
                        return 50  # Return the mode for hard difficulty
        pygame.display.flip()


# Function to draw the Sudoku board
def draw_sudoku_board(screen, sudoku_board):
   global cell_status
   rv = -1
   rh = -1
   hv = 0
   hh = 0
   for i in range(board_size + 1):
       rh += 1
       if rh == 3 and hh != 2:
           pygame.draw.line(screen, (0, 0, 0), (board_x, board_y + i * cell_size),
                        (board_x + board_width, board_y + i * cell_size), 6)
           rh = 0
           hh += 1
       else:
           pygame.draw.line(screen, (0, 0, 0), (board_x, board_y + i * cell_size),
                            (board_x + board_width, board_y + i * cell_size), 2)
   for i in range(board_size + 1):
       rv += 1
       if rv == 3 and hv != 2:
            pygame.draw.line(screen, (0, 0, 0), (board_x + i * cell_size, board_y),
                            (board_x + i * cell_size, board_y + board_height), 6)
            rv = 0
            hv += 1
       else:
           pygame.draw.line(screen, (0, 0, 0), (board_x + i * cell_size, board_y),
                            (board_x + i * cell_size, board_y + board_height), 2)


   font = pygame.font.Font(None, 40)
   for i in range(board_size):
       for j in range(board_size):
           if sudoku_board[i][j] != 0:
               # Check if the cell contains an original number or a sketch
               if cell_status[i][j] == "original":
                   text_surface = font.render(str(sudoku_board[i][j]), True, boldTextColor)
               else:
                   text_surface = font.render(str(sudoku_board[i][j]), True, sketchColor)
               text_rect = text_surface.get_rect(center=(board_x + j * cell_size + cell_size // 2,
                                                          board_y + i * cell_size + cell_size // 2))
               screen.blit(text_surface, text_rect)


   # Highlight the selected cell
   pygame.draw.rect(screen, (255, 0, 0), (board_x + selected_cell[1] * cell_size,
                                          board_y + selected_cell[0] * cell_size, cell_size, cell_size), 3)


def generate_initial_grid():
   # Your code to generate the initial Sudoku grid dynamically
   # Example: generate a random Sudoku grid
   initial_grid = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
   return initial_grid


def reset_board(sudoku_board):
   global original_board, cell_status
   for i in range(board_size):
       for j in range(board_size):
           if cell_status[i][j] is not None and cell_status[i][j] != "original":
               sudoku_board[i][j] = original_board[i][j]
               cell_status[i][j] = None


# Event handling function
def handle_game_events(screen, sudoku_board, reset_button_rect, restart_button_rect, exit_button_rect, mode):
    global selected_cell

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row = (mouse_pos[1] - board_y) // cell_size
            col = (mouse_pos[0] - board_x) // cell_size
            if 0 <= row < board_size and 0 <= col < board_size:
                selected_cell = (row, col)
            if reset_button_rect.collidepoint(mouse_pos):
                reset_board(sudoku_board)
            elif restart_button_rect.collidepoint(mouse_pos):
                main()  # Restart the game
            elif exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in numbers:
                if cell_status[selected_cell[0]][selected_cell[1]] != "original":
                    new_value = int(pygame.key.name(event.key))
                    sudoku_board[selected_cell[0]][selected_cell[1]] = new_value
                    cell_status[selected_cell[0]][selected_cell[1]] = "sketch"
            elif event.key == pygame.K_RETURN:
                # Mark the current sketch as original
                if cell_status[selected_cell[0]][selected_cell[1]] == "sketch":
                    cell_status[selected_cell[0]][selected_cell[1]] = "original"

                # After setting the status, check if the board is completely filled
                if all(sudoku_board[i][j] != 0 for i in range(board_size) for j in range(board_size)):
                    if check_win(sudoku_board):
                        display_win_screen(screen)
                        return  # Exit the loop after winning
                    else:
                        display_lose_screen(screen)
                        return  # Exit the loop on loss
            elif event.key == pygame.K_BACKSPACE:
                if cell_status[selected_cell[0]][selected_cell[1]] != "original":
                    sudoku_board[selected_cell[0]][selected_cell[1]] = 0
                    cell_status[selected_cell[0]][selected_cell[1]] = None
            elif pygame.K_1 <= event.key <= pygame.K_9:
                typed_number = event.key - pygame.K_0
                if 1 <= typed_number <= 9 and cell_status[selected_cell[0]][selected_cell[1]] != "original":
                    sudoku_board[selected_cell[0]][selected_cell[1]] = typed_number
                    cell_status[selected_cell[0]][selected_cell[1]] = "sketch"
            # Arrow keys for moving selection
            elif event.key == pygame.K_UP:
                selected_cell = (max(0, selected_cell[0] - 1), selected_cell[1])
            elif event.key == pygame.K_DOWN:
                selected_cell = (min(board_size - 1, selected_cell[0] + 1), selected_cell[1])
            elif event.key == pygame.K_LEFT:
                selected_cell = (selected_cell[0], max(0, selected_cell[1] - 1))
            elif event.key == pygame.K_RIGHT:
                selected_cell = (selected_cell[0], min(board_size - 1, selected_cell[1] + 1))


# Function to check if the Sudoku board is solved correctly
def check_win(board):
    if any(board[i][j] == 0 for i in range(board_size) for j in range(board_size)):
        return False

        # Check rows and columns
    for i in range(board_size):
        if (len(set(board[i][j] for j in range(board_size))) != board_size) or \
                (len(set(board[j][i] for j in range(board_size))) != board_size):
            return False

        # Check 3x3 squares
    for x in range(0, board_size, 3):
        for y in range(0, board_size, 3):
            square = [board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]
            if len(set(square)) != board_size:
                return False

    return True
   # for row in range(board_size):
   #     for col in range(board_size):
   #         if board[row][col] == 0:
   #             return False
   #
   #
   # for row in range(board_size):
   #     for col in range(board_size):
   #         num = board[row][col]
   #         board[row][col] = 0
   #         if not is_valid(board, row, col, num):
   #             return False
   #         board[row][col] = num
   # return True


# Function to check if a move is valid
def is_valid(board, row, col, num):
   for j in range(board_size):
       if j != col and board[row][j] == num:
           return False


   for i in range(board_size):
       if i != row and board[i][col] == num:
           return False


   start_row, start_col = 3 * (row // 3), 3 * (col // 3)
   for i in range(start_row, start_row + 3):
       for j in range(start_col, start_col + 3):
           if (i != row or j != col) and board[i][j] == num:
               return False


   return True


# Function to check if the board is filled completely but incorrect
def board_is_full_but_incorrect(board):
   for row in range(board_size):
       for col in range(board_size):
           if board[row][col] == 0:
               return False


   return not check_win(board)


# Function to display win screen
def display_win_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("Congratulations! You solved the Sudoku puzzle!", True, (0, 128, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()


# Function to display lose screen
def display_lose_screen(screen):
    running = True
    font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 28)

    # Text for the lose message
    text = font.render("Sorry, you solved the Sudoku puzzle incorrectly!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))

    # Button details
    button_text = button_font.render("Restart", True, (0, 0, 0))
    button_rect = pygame.Rect(width // 2 - 50, height // 2 + 50, 100, 50)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    while running:
        screen.fill((255, 0, 0))  # Fill the screen with red color
        screen.blit(text, text_rect)  # Display the lose message
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Draw the button
        screen.blit(button_text, button_text_rect)  # Display the button text
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Check if the button is clicked
                    main()  # Restart the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                    running = False


def reset_board(sudoku_board):
   global original_board, cell_status
   for i in range(board_size):
       for j in range(board_size):
           #reset the cell to the original board value
           sudoku_board[i][j] = original_board[i][j]
           #reset the cell status to "original" if the cell contains a number, otherwise None
           cell_status[i][j] = "original" if original_board[i][j] != 0 else None




# Main function
def main():
   global original_board, cell_status
   pygame.init()
   screen = pygame.display.set_mode((width, height))


   mode = draw_game_start(screen)


   sudoku_board, _ = generate_sudoku(9, mode)
   original_board = [row[:] for row in sudoku_board]
   cell_status = [["original" if num != 0 else None for num in row] for row in sudoku_board]


   button_spacing = 20
   button_height = 40
   button_y = height - button_height - 20
   reset_button_rect = pygame.Rect(button_spacing, button_y, 100, button_height)
   restart_button_rect = pygame.Rect(width // 2 - 50, button_y, 100, button_height)
   exit_button_rect = pygame.Rect(width - 120, button_y, 100, button_height)


   while True:
       handle_game_events(screen, sudoku_board, reset_button_rect, restart_button_rect, exit_button_rect, mode)
       screen.fill(color="white")
       draw_sudoku_board(screen, sudoku_board)


       pygame.draw.rect(screen, (100, 100, 100), reset_button_rect)
       pygame.draw.rect(screen, (100, 100, 100), restart_button_rect)
       pygame.draw.rect(screen, (100, 100, 100), exit_button_rect)


       font = pygame.font.Font(None, 24)
       text_surface = font.render("Reset", True, (255, 255, 255))
       text_rect = text_surface.get_rect(center=reset_button_rect.center)
       screen.blit(text_surface, text_rect)


       text_surface = font.render("Restart", True, (255, 255, 255))
       text_rect = text_surface.get_rect(center=restart_button_rect.center)
       screen.blit(text_surface, text_rect)


       text_surface = font.render("Exit", True, (255, 255, 255))
       text_rect = text_surface.get_rect(center=exit_button_rect.center)
       screen.blit(text_surface, text_rect)


       pygame.display.flip()



if __name__ == "__main__":
   main()