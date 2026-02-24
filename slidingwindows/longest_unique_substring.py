def longest_unique_substring(s: str) -> int:
    characters = set()
    left = 0
    max_len = 0
    right = 0

    while right < len(s):
        while s[right] in characters:
            characters.remove(s[left])
            left += 1

        characters.add(s[right])
        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len

def test_longest_unique_substring():
    assert longest_unique_substring("abcba") == 3
