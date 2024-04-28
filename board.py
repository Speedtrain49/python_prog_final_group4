import pygame, sys
from sudoku_generator import generate_sudoku
from cell import Cell

class Board:
    black = "black"
    cell_list = []
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.sudoku, self.ansSudoku = generate_sudoku(9,difficulty)

    def draw(self):
        self.cell_list = []
        xval = 55
        yval = 55
        bold = -1
        row = 0
        for i in range(9):
            bold += 1
            if bold == 3:
                pygame.draw.line(self.screen, self.black, (xval * i, 0), (xval * i, 500), 6)
                pygame.draw.line(self.screen, self.black, (0, yval * i), (500, yval * i), 6)
                bold = 0
            else:
                pygame.draw.line(self.screen, self.black, (xval*i,0), (xval*i,500), 2)
                pygame.draw.line(self.screen, self.black, (0, yval*i), (500, yval*i), 2)
        for b_list in self.sudoku:
            row += 1
            column = 0
            for value in b_list:
                column += 1
                n_cell = Cell(value, row, column, self.screen)
                n_cell.draw(False)
                if value > 0:
                    n_cell.set_static_cell_value(value)
                self.cell_list.append(n_cell)
                n_cell.draw(False)

    def select(self, col, row):
        for cell in self.cell_list:
            if cell.col == col and cell.row == row:
                cell.draw(True)
            else:
                cell.draw(False)
    def click(self, x, y):
        cords = ()
        if x >= 0 and x <= 500 and y >= 0 and y <= 500:
            for cell in self.cell_list:
                if x >= cell.coln-55 and x <= cell.coln and y >= cell.rown - 55 and y <= cell.rown:
                    cords = (cell.col, cell.row)
        else:
            return None
        return cords

    def clear(self, col ,row):
        for cell in self.cell_list:
            if cell.col == col and cell.row == row and cell.static == False:
                cell.value = 0
                cell.sketched = False
                cell.sketchedValue = 0
                cell.draw(True)

    def sketch(self, value, col, row):
        for cell in self.cell_list:
            if cell.col == col and cell.row == row and cell.static == False and cell.entered == False:
                cell.set_sketched_value(value)
                cell.draw(True)

    def place_number(self, col, row):
        for cell in self.cell_list:
            if cell.col == col and cell.row == row and cell.static == False and cell.sketeched == True:
                value = cell.sketchedValue
                cell.set_cell_value(value)
                cell.draw(True)

    def reset_to_original(self):
        self.cell_list = []
        self.draw()

    def is_full(self):
        count = 0
        for cell in self.cell_list:
            if cell.static == True or cell.entered == True:
                count += 1
        if count == 81:
            return True
        else:
            return False

    def check_board(self):
        input_list = []
        for cell in self.cell_list:
            input_list.apend(cell.set_value)