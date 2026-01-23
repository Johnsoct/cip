from typing import List


def findPivot(letters: List[str]) -> (int, int, List[str]):
    right = len(letters) - 1
    pivot = right - 1
    suffix = letters[pivot + 1:]

    while (pivot >= 0 and letters[pivot] >= letters[right]):
        right -= 1
        pivot -= 1
        suffix = letters[pivot + 1:]

    print(f'pivot: {pivot}; right {right}; suffix: {suffix}')

    return pivot, suffix


def findRightmostSuccessor(letters: List[str], pivot: int) -> int:
    rightmost_successor = len(letters) - 1

    print(rightmost_successor, letters)

    while (letters[rightmost_successor] <= letters[pivot]):
        rightmost_successor -= 1

    print(f'rightmost_successor: {rightmost_successor}; successor: {
          letters[rightmost_successor]}')

    return rightmost_successor


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

    letters = list(s)

    # Find the pivot by traversing the string backwards until you find a number which
    # is smaller than the previous
    pivot, suffix = findPivot(s)

    if (pivot == -1):
        return "".join(reversed(letters))

    # Rearrange the characters by replacing the pivot with the rightmost character which
    # is larger
    rightmost_successor = findRightmostSuccessor(letters, pivot)

    # Tuple assignment allows the tuple to be evaluated first instead of left to
    # right assighment, which would make `letters[pivot]` unreliable in the second
    # assignment
    letters[pivot], letters[rightmost_successor] = (
        letters[rightmost_successor], letters[pivot]
    )

    # Reverse the substring to the right of your pivot
    letters[pivot + 1:] = reversed(letters[pivot + 1:])

    # If no pivot is found, you're at the last lexicographical sequence, and you need to
    # reverse the string to get back to the first
    return "".join(letters)


def test_main():
    assert main("abc") == "acb"
    assert main("acb") == "bac"
    assert main("cba") == "abc"
    assert main("a") == "a"
    assert main("aaaa") == "aaaa"
    assert main("ynitsed") == "ynsdeit"
    assert main("abcd") == "abdc"
