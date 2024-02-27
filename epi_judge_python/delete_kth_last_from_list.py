from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(l: ListNode, k: int) -> Optional[ListNode]:
    sentinel = ListNode(0, l)

    kth_node = sentinel
    for _ in range(k + 1):
        kth_node = kth_node.next

    trailer = sentinel
    while kth_node:
        kth_node = kth_node.next
        trailer = trailer.next

    trailer.next = trailer.next.next

    return sentinel.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
