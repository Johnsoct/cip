def longest_uniform_substring_after_replacement(s: str, k: int) -> int:
    frequencies = {}
    highest_frequency = 0
    max_length = 0
    left = 0
    right = 0

    while right < len(s):
        # Update the frequency of the character at the right pointer
        # and the highest frequency for the current window
        frequencies[s[right]] = frequencies.get(s[right], 0) + 1
        highest_frequency = max(highest_frequency, frequencies[s[right]])

        # Calculate the replacements needed for the current window
        replacments_needed = (right - left + 1) - highest_frequency

        # Slide the window if the number of replacements needed exceed the limit
        # (the right pointer always advanced, so only handle the left
        if replacments_needed > k:
            frequencies[s[left]] -= 1
            left += 1

        max_length = right - left + 1
        right += 1

    return max_length

def test():
    assert longest_uniform_substring_after_replacement("aabcdcca", 2) == 5
