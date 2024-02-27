import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    print("----------")
    # size is number of chars to apply transform to
    # s is str arr to apply
    # Brute: scan s, marking indices that are 'a' or 'b'
    # "assume array is long enough" -- iterate from back and swap each element based on expected shift
    #   only works if array will have _more_ elements at end
    read_index = 0
    write_index = 0
    print(s)
    num_a = 0
    num_b = 0
    end_after_delete_b = 0
    for i in range(len(s)):
        if s[read_index] != 'b':
            if s[read_index] == '':
                end_after_delete_b = read_index
                while write_index < read_index:
                    s[write_index] = ''
                    write_index += 1
                break
            elif s[read_index] == 'a':
                num_a += 1
            s[write_index] = s[read_index]
            read_index += 1
            write_index += 1
        if s[read_index] == 'b':
            num_b += 1
            read_index += 1
    print(s)
    write_index = end_after_delete_b + (num_a) - 1
    cur_idx = end_after_delete_b - 1
    while cur_idx >= 0:
        if s[cur_idx] != 'a':
            s[write_index] = s[cur_idx]
            write_index -= 1
        else:
            s[write_index] = 'd'
            s[write_index - 1] = 'd'
            write_index -= 2
        cur_idx -= 1
    print(s)
    return size + num_a - num_b


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
