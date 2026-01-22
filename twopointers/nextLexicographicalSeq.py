from typing import List


def main(s: str) -> str:
    """
        Rearranges the string's characters into a new string represent the next immediate
        lexicographical sequence.

        Lexicographical order is alphabetical order in a numerical sense.

        If "abc" is the first lexicographical sequence, "acb" is the next immediate sequence,
        because if "abc" equals 123 the next possible sequence is 132.

        If "cba" is the last lexicographical sequence, "abc" is the next immediate sequence,
        because it's the first possible sequence.
    """

    # Find the pivot by traversing the string backwards until you find a number which
    # is smaller than the previous
    right = len(s) - 1
    pivot = right + 1
    suffix = s[pivot + 1:]

    while (s[pivot] > s[right]):
        right -= 1
        pivot -= 1
        suffix = s[pivot + 1:]

    # Rearrange the characters by replacing the pivot with the rightmost character which
    # is larger
    right = len(suffix) - 1
    left = right + 1
    successor = suffix[left]
    while (suffix[left] < suffix[right]):
        left -= 1
        successor = suffix[left]

    s[pivot], s[left] = successor, s[pivot]

    # Reverse the substring to the right of your pivot
    s[pivot + 1:] = reversed(s[pivot + 1:])

    # If no pivot is found, you're at the last lexicographical sequence, and you need to
    # reverse the string to get back to the first


def test_main():
