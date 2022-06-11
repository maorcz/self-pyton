from board_output import Output
from data_holder import DataHolder
from logging_testing import log_print


class Instructions:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.upper_instructions = []
        self.idx_upper = 0

        self.left_instructions = []
        self.idx_left = 0

    def __str__(self):
        twod_empty_img = Image('?', self.cols, self.rows).get_2dlist()
        return Output.output_board(self.left_instructions,
                                   self.upper_instructions,
                                   twod_empty_img)

    def is_set_appropriately(self):
        return self.idx_upper == self.cols and self.idx_left == self.rows

    def add_upper_instruction(self, *args):
        if self.idx_upper == self.cols:
            raise Exception(
                "You're using the function too many times.\
                 pay attention to boolean value ")
        new_list = []
        for item in args:
            new_list.append(item)

        self.upper_instructions.append(new_list)
        self.idx_upper += 1
        return self.idx_upper < self.cols

    def get_upper_instructions(self):
        if self.idx_upper == self.cols:
            return self.upper_instructions
        else:
            return []

    def add_left_instruction(self, *args):
        if self.idx_left == self.rows:
            raise Exception(
                "You're using the function too many times.\
                pay attention to boolean value ")
        new_list = []
        for item in args:
            new_list.append(item)

        self.left_instructions.append(new_list)
        self.idx_left += 1
        return self.idx_left < self.rows

    def get_left_instructions(self):
        if self.idx_left == self.rows:
            return self.left_instructions
        else:
            return []


class TwodKnowledge():
    def __init__(self, instructions):
        self.instructions = instructions
        cols = instructions.cols
        rows = instructions.rows

        self.counter = 0
        self.total_knowledges = \
            len(instructions.upper_instructions[0]) * cols +\
            len(instructions.left_instructions[0]) * rows

        self.upper_list_knowledges = []
        self.left_list_knowledges = []

        for line_instruction in instructions.upper_instructions:
            line_knowledge = self._make_line_knowledge_from_instructions(
                'left', line_instruction, rows)
            self.upper_list_knowledges.append(line_knowledge)

        for line_instruction in instructions.left_instructions:
            line_knowledge = self._make_line_knowledge_from_instructions(
                'up', line_instruction, cols)
            self.left_list_knowledges.append(line_knowledge)

    def _make_line_knowledge_from_instructions(self, left_or_up: str,
                                               line_instr, num_cells):
        min_consequtive_cells = len(line_instr) - 1
        for num_sequence in line_instr:
            if num_sequence == 0:
                min_consequtive_cells -= 1
            else:
                min_consequtive_cells += num_sequence

        odef = num_cells - min_consequtive_cells  # should always be >=0
        list_knowledges = []
        start_idx = 0
        for idx_instr, num_sequence in enumerate(line_instr):
            end_idx = start_idx + num_sequence + \
                odef if num_sequence > odef else num_cells
            list_of_ranges = []
            list_of_ranges.append([start_idx, end_idx])

            knowledge = Knowledge(num_sequence, list_of_ranges)
            list_knowledges.append(DataHolder(knowledge))

            if num_sequence != 0:
                start_idx += num_sequence + 1
            elif not knowledge.is_marked:
                knowledge.is_marked = True
                self.counter += 1

        return list_knowledges

    def __str__(self):
        res = 'upper knowledge:\n'
        for line in self.upper_list_knowledges:
            res += '\t' + str(line) + '\n'

        res += 'left knowledge:\n'
        for line in self.left_list_knowledges:
            res += '\t' + str(line) + '\n'

        return res + f'counter {self.counter} of {self.total_knowledges}'

    def get_list_knowledges(self, left_or_up: str):
        if left_or_up == 'left':
            return self.left_list_knowledges
        elif left_or_up == 'up':
            return self.upper_list_knowledges
        else:
            raise Exception(f'left_or_up was: "{left_or_up}"')

    def is_all_set(self):
        return self.counter == self.total_knowledges

    def _is_line_knowledge_set(self, line_knowledges):
        for data in line_knowledges:
            knowledge = data.get_value()
            if not knowledge.is_marked:
                return False
        return True


class Image:
    def __init__(self, init_data, cols, rows):
        self.cols = cols
        self.rows = rows
        self.twod_list = [[DataHolder(init_data) for j in range(cols)]
                          for i in range(rows)]

    def __str__(self):
        return Output.output_image(self.twod_list)

    def get_list_rows(self, idx_row):
        return self.twod_list[idx_row]

    def get_list_cols(self, idx_col):
        list_cols = []

        for list_row in self.twod_list:
            list_cols.append(list_row[idx_col])
        return list_cols

    def get_list(self, left_or_up: str, idx):
        if left_or_up == 'left':
            return self.get_list_rows(idx)
        elif left_or_up == 'up':
            return self.get_list_cols(idx)
        else:
            raise Exception(f'left_or_up was: "{left_or_up}"')

    def get_2dlist(self):
        return self.twod_list

    def set_cell(self, idx_row, idx_col, new_val):
        self.twod_list[idx_row][idx_col].set_value(new_val)


class Board:
    def __init__(self, instructions: Instructions):
        self.twod_knowledge = TwodKnowledge(instructions)
        self.image = Image('?', self.get_cols(), self.get_rows())

    def __str__(self):
        return Output.output_board(
            self.twod_knowledge.instructions.left_instructions,
            self.twod_knowledge.instructions.upper_instructions,
            self.image.get_2dlist())

    def get_cols(self):
        return self.twod_knowledge.instructions.cols

    def get_rows(self):
        return self.twod_knowledge.instructions.rows


class Knowledge():
    def __init__(self, num_sequence, list_of_ranges, is_marked=False):
        if num_sequence is None or list_of_ranges is None:
            raise Exception('Knowledge argument is None')

        self.is_marked = is_marked
        self.num_sequence = num_sequence
        self.list_of_ranges = list_of_ranges

    def __str__(self):
        a = "_" if self.is_marked else "X"
        return f'{a}_{self.num_sequence}_rngs{self.list_of_ranges}'

    def set_as_marked(self, twod_knowledge, left_or_up, idx_table):
        if not self.is_marked:
            self.is_marked = True
            twod_knowledge.counter += 1

            return twod_knowledge._is_line_knowledge_set(
                twod_knowledge.get_list_knowledges(left_or_up)[idx_table])

    def pop_range(self, idx):
        if len(self.list_of_ranges) > 1:
            self.list_of_ranges.pop(idx)
        else:
            raise Exception(
                'trying to empty the list before knowledge was marked')

    def insert_range(self, idx, range):
        max_sequence_fitting = range[1] - range[0]

        if self.num_sequence <= max_sequence_fitting:
            self.list_of_ranges.insert(idx, range)
        # note: else: the new range doesnt big enough

    def compact_ranges_by_forbidden_sequence(self, idx_from, idx_to):
        for idx_list, rangee in enumerate(self.list_of_ranges):
            at_least_one_in_range = rangee[0] < idx_to and rangee[1] > idx_from

            if at_least_one_in_range:
                self.list_of_ranges.pop(idx_list)

                if rangee[1] <= idx_to:
                    rangee[1] = idx_from
                else:
                    self.insert_range(idx_list, [idx_to, rangee[1]])

                if rangee[0] >= idx_from:
                    rangee[0] = idx_to
                else:
                    self.insert_range(idx_list, [rangee[0], idx_from])
