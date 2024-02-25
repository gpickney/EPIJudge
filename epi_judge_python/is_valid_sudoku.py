import pdb
from collections import defaultdict
from typing import List, Tuple, Dict

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    subgrids: Dict[Tuple[int, int], List[int]] = defaultdict(list)
    for row_idx, row in enumerate(partial_assignment):
        for col_idx, col_val in enumerate(row):
            subgrid_id = (int(row_idx / 3), int(col_idx / 3))
            subgrids[subgrid_id].append(col_val)

    for subgrid_id, subgrid in subgrids.items():
        if not list_is_unique(subgrid):
            return False

    cols = [[]*9 for _ in range(9)]
    for row_idx, row in enumerate(partial_assignment):
        for col_idx, col in enumerate(row):
            cols[col_idx].append(col)
        if not list_is_unique(row):
            return False

    for col in cols:
        if not list_is_unique(col):
            return False

    return True


def list_is_unique(row):
    digits_seen = set()
    for digit in row:
        if digit == 0:
            continue
        elif digit in digits_seen:
            return False
        else:
            digits_seen.add(digit)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
