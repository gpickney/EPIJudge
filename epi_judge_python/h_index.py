from typing import List
from collections import Counter
from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citation_counts = Counter()
    for num_citations in citations:
        citation_counts[num_citations] += 1

    # print(citation_counts)
    sorted(citation_counts, reverse=True)
    max_h_index = len(citations)
    # print(f"Max h-index is {max_h_index}")
    for i in range(max_h_index, -1, -1):
        ge_i_count = 0
        # print(f"Is h-index {i}?")
        for citation_count, times_seen in citation_counts.items():
            # print(f"\tCitation count: {citation_count} seen {times_seen} times")
            if citation_count >= i:
                ge_i_count += times_seen
            if ge_i_count >= i:
                return i
            # else:
            #     print(f"\tge_i_count: {ge_i_count}")
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
