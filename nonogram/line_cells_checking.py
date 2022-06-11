from data_holder import DataHolder


class LineCellsChecker:
    def _get_sequence(cell_val, from_idx, line_holders):
        num = 0
        for idx in range(from_idx, len(line_holders)):
            if line_holders[idx].get_value() != cell_val:
                break
            num += 1
        return num


if __name__ == '__main__':
    test_lines = [[DataHolder('a'), DataHolder('b'), DataHolder('a')],
                  [DataHolder('a'), DataHolder('a'), DataHolder('a')],
                  [DataHolder('a'), DataHolder('a'), DataHolder('a')]]

    print(1 == LineCellsChecker._get_sequence('a', 0, test_lines[0]))
    print(2 == LineCellsChecker._get_sequence('a', 1, test_lines[1]))
    print(0 == LineCellsChecker._get_sequence('c', 2, test_lines[1]))
