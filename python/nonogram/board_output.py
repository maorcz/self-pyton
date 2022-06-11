class Output:
    def output_board(left_instructions, upper_instructions, img):
        out = Output._output_upper(
            len(left_instructions[0]), upper_instructions)
        out += Output._output_below(left_instructions, img)
        return out

    def output_image(img):
        out = ''
        for row in img:
            out += Output._output_narrow_line_data(row)
        return out

    def _char_data_to_output(ch):
        if ch == 'm':  # mark
            return '⬛'
        elif ch == 's':  # space
            return '⬜'
        elif ch == '?':
            return '  '
            # return '〇'
        else:
            return ch

    def _output_upper(len_left_instruction, upper_instructions):
        out = ''
        rows = len(upper_instructions[0])
        out += ' '*(2 * len_left_instruction) + '┬'
        out += '─┬'*(len(upper_instructions)-1) + '──┬\n'

        for idx_line in range(rows):
            out += ' '*(2*len_left_instruction)
            for sequence in upper_instructions:
                num = sequence[idx_line]
                out += '│'
                if num == 0:
                    out += ' '
                else:
                    out += f'{num}'
            out += ' │\n'

        for i in range(len_left_instruction):
            out += '┬─'
        out += '┼'+'─┴' * (len(upper_instructions)-1) + '──┼\n'

        return out

    def _output_row_instruction(instruction):
        out = ''
        for num in instruction:
            out += '│'
            if num == 0:
                out += ' '
            else:
                out += f'{num}'
        out += '│'
        return out

    def _output_line_data(line_data):
        out = ''
        for cell_data in line_data:
            out += Output._char_data_to_output(cell_data.get_value())
        out += '│\n'
        return out

    def _output_narrow_line_data(line_data):
        out = ''
        for cell_data in line_data:
            out += Output._char_data_to_output(cell_data.get_value())
        out += '\n'
        return out

    def _output_below(left_instructions, img):
        out = ''
        for idx_row in range(len(img)):
            out += Output._output_row_instruction(left_instructions[idx_row])
            out += Output._output_line_data(img[idx_row])

        out += '┴─' * len(left_instructions[0]) + '┴'
        out += '─' * (2 * len(img[0])) + '┴\n'
        return out
