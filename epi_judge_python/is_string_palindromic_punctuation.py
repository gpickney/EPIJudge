from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    right = len(s) - 1
    left = 0

    while right > left:
        while not s[right].isalnum() and right > left:
            right -= 1
        while not s[left].isalnum() and right > left:
            left += 1
        print(f"Comparing {s[left]} to {s[right]}")
        if s[left].lower() != s[right].lower():
            return False
        right -= 1
        left += 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
