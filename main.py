from sudoku_generator import SudokuGenerator

def main():

    #EVERYTHING HERE IS FOR TESTING
    p = SudokuGenerator(9, 10)
    # SudokuGenerator.valid_in_box(p, 7, 7, 9)
    # print(p.board)
    # p.board[0] = ['*', 1, '*', '*', '*', '*', '*', '*', '*']
    # p.board[1] = [1, 2, 3, 4, 5, 6, 7, 8, '*']
    # p.board[2] = ['*', 3, '*', '*', '*', '*', '*', '*', '*']
    # p.board[3] = ['*', 4, '*', '*', '*', '*', '*', '*', '*']
    # p.board[4] = ['*', 5, '*', '*', '*', '*', '*', '*', '*']
    # p.board[5] = ['*', 6, '*', '*', '*', '*', '*', '*', '*']
    # p.board[6] = ['*', 7, '*', '*', '*', '*', '*', '*', '*']
    # p.board[7] = ['*', 8, '*', '*', '*', '*', '*', '*', '*']
    # p.board[8] = ['*', 9, '*', '*', '*', '*', '*', '*', '*']
    #
    # print(p.board)
    # SudokuGenerator.is_valid(p, 1, 1, 9)
    p.fill_diagonal()
    p.print_board()
    print(" ")
    p.fill_remaining(0, 0)
    p.print_board()

if __name__ == "__main__":
    main()