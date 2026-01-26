def main(s: str) -> bool:
    """Determines whether a string is a palindrome in O(n) time."""

    left = 0
    right = len(s) - 1

    while left < right:
        # Make sure left represents an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1

        # Make sure right represents an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        if not s[left] == s[right]:
            return False

        left += 1
        right -= 1

    return True


def test_main():
    assert(main("")) == True
    assert(main("a")) == True
    assert(main("aa")) == True
    assert(main("!, (?)")) == True
    assert(main("12.02.2021")) == True
    assert(main("a dog! a panic in a pagoda.")) == True
    assert(main("ab")) == False
    assert(main("21.02.2021")) == False
    assert(main("hello, world!")) == False
    assert(main("abc123")) == False
