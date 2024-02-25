from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    max_pow = len(A) - 1
    num = 0
    for d in A:
        num += d * 10**max_pow
        max_pow -= 1
    num += 1
    return [int(d) for d in str(num)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
