import functools
import pdb
from collections import defaultdict

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_len(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    print("\nBEGIN")
    l0_len = list_len(l0)
    l1_len = list_len(l1)

    print(f"Length of l0: {l0_len}")
    print(f"Length of l1: {l1_len}")
    shorter = l1 if l1_len < l0_len else l0
    longer = l1 if l1_len >= l0_len else l0

    # Advance longer by difference in length
    n = abs(l1_len - l0_len)
    for _ in range(0, n):
        longer = longer.next

    # Now advance both until equal
    while longer and shorter and longer is not shorter:
        longer = longer.next
        shorter = shorter.next

    return shorter


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
