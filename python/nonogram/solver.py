from board import Board, Knowledge
from task import Task
from heapq import heappush, heappop
from line_cells_checking import LineCellsChecker
from logging_testing import log_print


def fit_in_range(num_sequence, line_cells, range_scope):
    start_idx = range_scope[0]
    for idx in range(start_idx, range_scope[1]):
        if line_cells[idx].get_value() == 's':
            is_big_enough = num_sequence <= range_scope[1] - start_idx
            if is_big_enough:
                return True
            start_idx = idx

    is_big_enough = num_sequence <= range_scope[1] - start_idx
    return is_big_enough


class Solver:
    def __init__(self, board: Board):
        self.board = board
        self.queue_tasks = []

    def solve(self):
        self._traverse_knowledges('left')
        self._traverse_knowledges('up')

        while not self.board.twod_knowledge.is_all_set():
            try:
                self._execute_task_by_queue()
            except Exception as e:
                print('EXCEPTION WAS RAISED: ', e)
                print(self.board.twod_knowledge)
                break

        return self.board  # optional

    def _update_line_knowledge_and_cells(self, left_or_up, idx):
        self._update_line_knowledge_by_cells(left_or_up, idx)
        counter_changed = self._update_line_cells_by_knowledge(left_or_up, idx)

        if counter_changed:
            self._update_line_knowledge_and_cells(left_or_up, idx)

    def _update_line_knowledge_by_cells(self, left_or_up, idx):  # todo
        line_knowledges = \
            self.board.twod_knowledge.get_list_knowledges(left_or_up)[idx]
        line_cells = self.board.image.get_list(left_or_up, idx)

        for data_holder in line_knowledges:
            knowledge = data_holder.get_value()

            num_sequence = knowledge.num_sequence
            for idx, range in enumerate(knowledge.list_of_ranges):
                if not fit_in_range(num_sequence, line_cells, range):
                    knowledge.pop_range(idx)

        idx = 0
        while idx < len(line_cells):
            cell_val = line_cells[idx].get_value()
            sequence_of_same = LineCellsChecker._get_sequence(
                cell_val, idx, line_cells)

            if cell_val == 's':
                for data_holder in line_knowledges:
                    knowledge = data_holder.get_value()
                    knowledge.compact_ranges_by_forbidden_sequence(
                        idx, idx + sequence_of_same)
                idx += sequence_of_same

            # elif cell_val == 'm':
            #     knowledge = _get_first_opened_knowledge(line_knowledges)
            #     if knowledge:
            #         reduce_ranges_of_knowledge

            idx += 1

    def _update_line_cells_by_knowledge(self, left_or_up, idx_table) -> int:
        line_knowledges = \
            self.board.twod_knowledge.get_list_knowledges(left_or_up)[
                idx_table]

        counter_changes = 0
        for idx_knowledge in range(len(line_knowledges)):
            knowledge = line_knowledges[idx_knowledge].get_value()

            num_sequence = knowledge.num_sequence
            list_of_ranges = knowledge.list_of_ranges

            if len(list_of_ranges) == 1:
                range_pair = list_of_ranges[0]
                start_mark_idx = range_pair[1] - num_sequence
                end_mark_idx = num_sequence + range_pair[0]

                for idx_to_mark in range(start_mark_idx, end_mark_idx):
                    counter_changes += self._change_and_log(
                        'm', left_or_up, idx_table, idx_to_mark)

                if end_mark_idx-start_mark_idx == num_sequence:
                    is_line_knowledge_set = \
                        knowledge.set_as_marked(self.board.twod_knowledge,
                                                left_or_up,
                                                idx_table)
                    if is_line_knowledge_set:
                        counter_changes += self.mark_blank_cells_as_spaces(
                            self.board.image.get_list(left_or_up, idx_table))

                    counter_changes += self._change_and_log(
                        's', left_or_up, idx_table, start_mark_idx - 1)
                    counter_changes += self._change_and_log(
                        's', left_or_up, idx_table, end_mark_idx)

        return counter_changes

    def _execute_task_by_queue(self):
        if len(self.queue_tasks) == 0:
            raise Exception(
                'queue is empty but there are still left knowledges to solve')

        task = heappop(self.queue_tasks)
        key_updated_line = task.key_check_line.split('_')
        left_or_up = key_updated_line[0]
        idx = int(key_updated_line[1])

        # for now: I dont care about the set of idxs in the dictionary
        task.pop_dict_from_super_dict()
        del task

        self._update_line_knowledge_and_cells(left_or_up, idx)

    def _traverse_knowledges(self, left_or_up):
        relevent_list_knowledges = \
            self.board.twod_knowledge.get_list_knowledges(left_or_up)

        for idx, line_knowledge in enumerate(relevent_list_knowledges):
            self._update_line_knowledge_and_cells(left_or_up, idx)

            is_line_knowledge_set = \
                self.board.twod_knowledge._is_line_knowledge_set(
                    line_knowledge)
            if is_line_knowledge_set:
                self.mark_blank_cells_as_spaces(
                    self.board.image.get_list(left_or_up, idx))

    def _change_and_log(self, mark_request, left_or_up, idx_table, idx_line):
        if mark_request is None or left_or_up not in ('left', 'up') \
                or idx_table is None or idx_line is None:
            raise Exception('Illegal arguments')

        is_changed = False
        line_cells = self.board.image.get_list(left_or_up, idx_table)

        if 0 <= idx_line < len(line_cells):
            data = line_cells[idx_line]
            cell_val = data.get_value()
            if cell_val != '?':
                if mark_request != cell_val:
                    msg = f'trying to write {mark_request} to a {cell_val} \
                        cell idx={idx_table}'
                    raise Exception(msg)

            else:
                is_changed = True

            if cell_val == '?':
                data.set_value(mark_request)

                line_knowledge = self.board.twod_knowledge.get_list_knowledges(
                    left_or_up)[idx_table]
                for new_idx, new_data in enumerate(line_knowledge):
                    if new_idx != idx_line:
                        knowledge = new_data.get_value()
                        knowledge.compact_ranges_by_forbidden_sequence(
                            idx_line,
                            idx_line + 1)

            self._push_to_queue(
                Task.opposite_left_or_up(left_or_up),
                idx_table,
                idx_line)

        return is_changed

    def _push_to_queue(self, new_left_or_up, idx_table, idx_line):
        allready_in_queue = False
        if Task.is_in_dictionary(self.board, new_left_or_up, idx_table):
            allready_in_queue = True

        task = Task(self.board, new_left_or_up,
                    idx_table=idx_line, idx_line=idx_table)

        if not allready_in_queue:
            heappush(self.queue_tasks, task)

    def mark_blank_cells_as_spaces(self, line_cell):
        counter_changed = 0

        for data in line_cell:
            if data.get_value() == '?':
                data.set_value('s')
                counter_changed += 1

        return counter_changed
