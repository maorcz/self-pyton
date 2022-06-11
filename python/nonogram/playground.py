from solver import Solver
from custom_input import CustomInput


def solve_and_print(board):
    solver = Solver(board)

    print('#' * 80, end='\n\n')
    solver.solve()

    print('\nresult:')
    print(board)


if __name__ == '__main__':
    solve_and_print(CustomInput.define_board_1x5_1())
    solve_and_print(CustomInput.define_board_3x5_1())
    solve_and_print(CustomInput.define_board_3x5_2())

    solve_and_print(CustomInput.define_board_5x5_1())
    solve_and_print(CustomInput.define_board_5x5_2())
    solve_and_print(CustomInput.define_board_10x10_1())
    solve_and_print(CustomInput.define_board_10x10_2())
