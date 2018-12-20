# https://projecteuler.net/problem=4
import cProfile


def simple_palindrome_mul(digit1: int, digit2: int):
    # Time O(n^2)
    def max_number(digit: int):
        return int("".join(["9"] * digit))

    top1, top2 = max_number(digit1), max_number(digit2)

    for index1 in range(top1 + 1):
        for index2 in range(top2 + 1):
            mul = index1 * index2
            if is_palindrome_number(mul):
                yield mul


def is_palindrome_number(number: int):
    str_n = str(number)
    return str_n == str_n[::-1]


if __name__ == "__main__":
    assert is_palindrome_number(99) is True
    assert is_palindrome_number(101) is True
    assert is_palindrome_number(3324334233) is True
    cProfile.run('print(max(simple_palindrome_mul(3, 3)))')
