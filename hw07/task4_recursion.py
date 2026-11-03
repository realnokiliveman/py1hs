def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def is_palindrome(text):
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])


print(count_digits(0), count_digits(7), count_digits(2026))
print(power(2, 10), power(5, 0))
print(is_palindrome("racecar"), is_palindrome("level"), is_palindrome("python"))