from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not (l1 and l2):
        return l1 if l1 else l2
    sentinel = ListNode(-1)
    node = sentinel
    while l1 and l2:
        if l1.data <= l2.data:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    node.next = l1 or l2
    return sentinel.next


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sorted_lists_merge.py', 'sorted_lists_merge.tsv', merge_two_sorted_lists))
