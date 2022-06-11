from functools import total_ordering
from board import Board
from logging_testing import log_print


@total_ordering
class Task:
    board_super_dict = {}

    def __init__(self, board: Board, left_or_up: str, idx_table, idx_line):
        if left_or_up not in ('left', 'up'):
            raise Exception(f"left_or_up is '{left_or_up}' {type(left_or_up)}")

        self.board = board
        self.key_board = hash(board)
        self.key_check_line = f'{left_or_up}_{idx_table}'

        if self.key_board not in Task.board_super_dict:
            Task.board_super_dict[self.key_board] = dict()

        if self.key_check_line not in Task.board_super_dict[self.key_board]:
            self.pop_dict_from_super_dict()
        Task.board_super_dict[self.key_board][self.key_check_line].add(
            idx_line)

    def pop_dict_from_super_dict(self):
        Task.board_super_dict[self.key_board][self.key_check_line] = set(
        )

    def __lt__(self, other):
        # todo problem -> priority changes while task in the heap
        return self._priority() > other._priority()

    def __eq__(self, other):
        return self._priority() == other._priority()

    def _priority(self):
        return len(Task.board_super_dict[self.key_board][self.key_check_line])

    def is_in_dictionary(board, left_or_up, idx_table):
        board_key = hash(board)
        key_check_line = f'{left_or_up}_{idx_table}'

        return board_key in Task.board_super_dict \
            and key_check_line in Task.board_super_dict[board_key]

    def opposite_left_or_up(left_or_up) -> str:
        if left_or_up == 'left':
            return 'up'
        elif left_or_up == 'up':
            return 'left'
        else:
            raise Exception(f'left_or_up was: "{left_or_up}"')


if __name__ == '__main__':
    board = 'test'
    t01 = Task(board, 'up', 0)
    t02 = Task(board, 'up', 0)
    t03 = Task(board, 'up', 0)
    t10 = Task(board, 'up', 1)
    t11 = Task(board, 'up', 1)
    t20 = Task(board, 'up', 2)

    print(t01 == t02)
    print(t01 == t03)
    print(t10 == t11)

    print(t01 < t10)
    print(t02 < t11)
    print(t02 < t10)
    print(t10 < t20)
