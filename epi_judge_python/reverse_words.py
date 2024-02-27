import functools
from collections import deque

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
# store slice of last word temporarily
# ->
# ['r','a','m',' ','i','s',' ','','','','r','a','m']
# copy n letters of first word into last n letters of second word
# slide every element in array before first index of second word over by the number of elements
def reverse_words(s):
    left = 0
    right = len(s)-1

    # Reverse array with swaps
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # Get (left, right) for each word
    words = []
    word_start = 0
    for i in range(len(s)):
        if s[i] == " " or i == len(s) - 1:
            if s[i] == " ":
                word_end = i-1
            else:
                word_end = i
            words.append((word_start, word_end))
            word_start = i+1

    # for each word bounded by (left, right), reverse word
    for left, right in words:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
