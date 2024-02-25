import math
from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    print("\n------------------------\n")
    n = len(square_matrix)
    shells_to_process = math.ceil(n / 2)
    shells_assembled = []
    if len(square_matrix) == 1:
        return [square_matrix[0][0]]
    else:
        while shells_to_process > 0:
            # Get shell order
            print(square_matrix)
            shells_assembled.extend(get_outer_shell(square_matrix))
            # print(f"\t so far we at: {shells_assembled}")
            # Get next inner matrix to process
            new_mat = []
            for i, row in enumerate(square_matrix):
                if i > 0 and i < n-1:
                    new_mat.append(row[1:n-1])
            square_matrix = new_mat
            n = len(new_mat)
            print(f"\tnew mat: {new_mat}")
            shells_to_process -= 1
    return shells_assembled


def get_outer_shell(matrix):
    print("processing shell...")
    n = len(matrix)
    # If shell is middle of odd nxn matrix, return just value in list
    if n == 1:
        return [matrix[0][0]]
    right = []
    down = []
    left = []
    up = []
    for row_idx, row in enumerate(matrix):
        for col_idx, col_val in enumerate(row):
            # right
            if row_idx == 0:
                right.append(col_val)
            # down
            elif col_idx == n - 1 and row_idx > 0:
                down.append(col_val)
            # left
            elif row_idx == n-1 and col_idx <= n-2:
                left.append(col_val)
            # up
            elif col_idx == 0 and 0 < row_idx <= n - 2:
                up.append(col_val)

    return right + down + left[::-1] + up[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
