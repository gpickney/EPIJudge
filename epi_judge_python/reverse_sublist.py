from typing import Optional

from list_node import ListNode
from test_framework import generic_test

from collections import deque


def reverse_sublist(head: ListNode, start: int, finish: int) -> Optional[ListNode]:
    sentinel = ListNode(-1, head)
    cur_idx = 0
    cur_node = sentinel
    nodes_to_swap = deque()
    while cur_idx <= finish:
        if start - 1 <= cur_idx <= finish:
            nodes_to_swap.append(cur_node)
        cur_idx += 1
        cur_node = cur_node.next

    left_preceding = nodes_to_swap.popleft() if nodes_to_swap else None
    while nodes_to_swap:
        if len(nodes_to_swap) == 1:
            # dont need to swap middle
            break
        right_preceding = nodes_to_swap[-2]
        left = nodes_to_swap.popleft()
        right = nodes_to_swap.pop()
        swap_nodes(left, right, left_preceding, right_preceding)
        # preceding node of next smaller sublist is "new" left
        left_preceding = right

    return sentinel.next


def swap_nodes(left: ListNode, right: ListNode, left_preceding: ListNode, right_preceding: ListNode):
    left_preceding.next = right
    old_right_next = right.next
    right.next = left.next if left.next != right else left  # Handle edge case of node being swapped adjacent
    left.next = old_right_next
    right_preceding.next = left if left != right_preceding else right_preceding.next  # Handle edge case of node being swapped adjacent


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
