import math
import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(self.row_length))

    def valid_in_box(self, row, col, num):
        box_row_start = row - row % self.box_length
        box_col_start = col - col % self.box_length
        for i in range(box_row_start, box_row_start + self.box_length):
            for j in range(box_col_start, box_col_start + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row, col, num))

    def fill_box(self, row, col):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row + i][col + j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length or col >= self.row_length:
            return True
        if col < self.box_length and row < self.box_length:
            col = self.box_length
        elif row >= self.box_length and row < self.row_length - self.box_length:
            if col == (row // self.box_length) * self.box_length:
                col += self.box_length
        elif row >= self.row_length - self.box_length:
            if col >= self.row_length - self.box_length:
                col = 0
                row += 1
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def remove_cells(self):
        positions = []
        for row in range(self.row_length):
            for col in range(self.row_length):
                positions.append((row, col))
        random.shuffle(positions)

        for i in range(self.removed_cells):
            if positions:
                row, col = positions.pop()
                self.board[row][col] = 0

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 0)

def generate_sudoku(size, removed):
    try:
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        return sudoku.board, True  # Return the board and a success status
    except Exception as e:
        return None, False
    sudoku.remove_cells

# Test the generator
board = generate_sudoku(9, 40)
for row in board:
    print(row)
