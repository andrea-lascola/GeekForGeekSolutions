# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square(num: int) -> int:
    return num * num


def square_diff(limit: int) -> int:
    num, sq_sum = 0, 0

    for n in range(limit + 1):
        num += n
        sq_sum += square(n)

    return square(num) - sq_sum


if __name__ == "__main__":
    assert square_diff(10) == 2640

    print(square_diff(100))
