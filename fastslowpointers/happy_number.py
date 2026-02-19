def get_next_num(n: int) -> int:
    """Returns the last digit in `n`"""

    num = n
    next_num = 0

    while num > 0:
        # Extract the last digit
        digit = num % 10

        # Truncate the last digit from `n` using floor division
        num //= 10

        next_num += digit ** 2

    return next_num

def is_happy_number(n: int) -> bool:
    """
    Returns True if `n` is a happy number, or a number which the repeatedly summing ths squaring
    its digits eventually results in 1

    Uses Floyd's Cycle Detection algorithm to determine if repeatedly summing the squares results in
    a cycle.
    """

    fast = n
    slow = n

    while True:
        fast = get_next_num(get_next_num(fast))
        slow = get_next_num(slow)

        if fast == 1:
            return True

        # Cycle detected
        elif slow == fast:
            return False

def test_is_happy_number():
    assert is_happy_number(23) == True
    assert is_happy_number(22) == False
