from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
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


if __name__ == "__main__":
    main()