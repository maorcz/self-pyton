from board import Board, Instructions


class CustomInput:
    def define_board_1x5_1():
        instr = Instructions(1, 5)

        instr.add_upper_instruction(1)
        instr.add_upper_instruction(0)
        instr.add_upper_instruction(1)
        instr.add_upper_instruction(0)
        instr.add_upper_instruction(1)

        instr.add_left_instruction(1, 1, 1)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_3x5_1():
        instr = Instructions(3, 5)

        instr.add_upper_instruction(1, 1)
        instr.add_upper_instruction(0, 0)
        instr.add_upper_instruction(1, 1)
        instr.add_upper_instruction(0, 0)
        instr.add_upper_instruction(1, 1)

        instr.add_left_instruction(1, 1, 1)
        instr.add_left_instruction(0, 0, 0)
        instr.add_left_instruction(1, 1, 1)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_3x5_2():
        instr = Instructions(3, 5)

        instr.add_upper_instruction(1, 1)
        instr.add_upper_instruction(0, 1)
        instr.add_upper_instruction(1, 1)
        instr.add_upper_instruction(0, 1)
        instr.add_upper_instruction(1, 1)

        instr.add_left_instruction(1, 1, 1)
        instr.add_left_instruction(0, 1, 1)
        instr.add_left_instruction(1, 1, 1)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_5x5_1():
        instr = Instructions(5, 5)

        instr.add_upper_instruction(3)
        instr.add_upper_instruction(1)
        instr.add_upper_instruction(5)
        instr.add_upper_instruction(1)
        instr.add_upper_instruction(3)

        instr.add_left_instruction(1, 1, 1)
        instr.add_left_instruction(1, 1, 1)
        instr.add_left_instruction(1, 1, 1)
        instr.add_left_instruction(0, 0, 3)
        instr.add_left_instruction(0, 0, 1)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_5x5_2():
        instr = Instructions(5, 5)

        instr.add_upper_instruction(4)
        instr.add_upper_instruction(3)
        instr.add_upper_instruction(4)
        instr.add_upper_instruction(1)
        instr.add_upper_instruction(1)

        instr.add_left_instruction(0, 1)
        instr.add_left_instruction(3, 1)
        instr.add_left_instruction(0, 4)
        instr.add_left_instruction(1, 1)
        instr.add_left_instruction(1, 1)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_10x10_1():
        instr = Instructions(10, 10)

        instr.add_upper_instruction(0, 0, 0, 1)
        instr.add_upper_instruction(0, 0, 4, 2)
        instr.add_upper_instruction(0, 0, 1, 2)
        instr.add_upper_instruction(0, 0, 6, 1)
        instr.add_upper_instruction(0, 1, 2, 1)
        instr.add_upper_instruction(0, 5, 1, 1)
        instr.add_upper_instruction(1, 2, 1, 1)
        instr.add_upper_instruction(0, 3, 1, 2)
        instr.add_upper_instruction(0, 0, 1, 5)
        instr.add_upper_instruction(0, 0, 0, 2)

        instr.add_left_instruction(0, 0, 0, 6)
        instr.add_left_instruction(1, 1, 1, 1)
        instr.add_left_instruction(0, 2, 1, 2)
        instr.add_left_instruction(1, 1, 2, 1)
        instr.add_left_instruction(0, 1, 1, 4)
        instr.add_left_instruction(0, 1, 2, 1)
        instr.add_left_instruction(0, 0, 0, 8)
        instr.add_left_instruction(0, 0, 1, 1)
        instr.add_left_instruction(0, 0, 1, 4)
        instr.add_left_instruction(0, 0, 0, 2)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None

    def define_board_10x10_2():
        instr = Instructions(10, 10)

        instr.add_upper_instruction(0, 0, 2)
        instr.add_upper_instruction(0, 2, 4)
        instr.add_upper_instruction(1, 6, 1)
        instr.add_upper_instruction(0, 5, 3)
        instr.add_upper_instruction(0, 4, 3)
        instr.add_upper_instruction(0, 1, 4)
        instr.add_upper_instruction(0, 0, 9)
        instr.add_upper_instruction(1, 6, 1)
        instr.add_upper_instruction(0, 2, 4)
        instr.add_upper_instruction(0, 0, 2)

        instr.add_left_instruction(0, 0, 2, 2)
        instr.add_left_instruction(0, 2, 4, 2)
        instr.add_left_instruction(1, 3, 2, 1)
        instr.add_left_instruction(0, 0, 4, 3)
        instr.add_left_instruction(0, 0, 4, 3)
        instr.add_left_instruction(0, 0, 3, 4)
        instr.add_left_instruction(0, 0, 2, 5)
        instr.add_left_instruction(0, 0, 0, 6)
        instr.add_left_instruction(0, 0, 0, 4)
        instr.add_left_instruction(0, 0, 2, 2)

        if instr.is_set_appropriately():
            return Board(instr)
        else:
            return None


if __name__ == '__main__':
    print(CustomInput.define_board_1x5_1())
    print(CustomInput.define_board_3x5_1())
    print(CustomInput.define_board_3x5_2())
    print(CustomInput.define_board_5x5_1())
    print(CustomInput.define_board_5x5_2())
    print(CustomInput.define_board_10x10_1())
    print(CustomInput.define_board_10x10_2())
