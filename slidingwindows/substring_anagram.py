def get_anagram_count(s: str, a: str) -> int:
    len_a = len(a)
    len_s = len(s)

    if len_a > len_s:
        return 0

    count = 0
    expected_frequencies = [0] * 26
    frequencies = [0] * 26
    left = 0
    right = 0

    for char in a:
        expected_frequencies[ord(char) - ord("a")] += 1

    while right < len_s:
        # Add the right pointer to the frequencies
        frequencies[ord(s[right]) - ord("a")] += 1

        # If the current window is of equal length to the anagram
        if right - left + 1 == len_a:
            # Increase the count if the current frequency is equal to the expectation
            if frequencies == expected_frequencies:
                count += 1

            # Subtract the left pointer from the frequencies before updating the left pointer
            frequencies[ord(s[left]) - ord("a")] -= 1

            left += 1

        right += 1

    return count

def test_get_anagram_count():
    assert get_anagram_count("caabab", "aba") == 2
