# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import itertools


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_prime(number: int = 10001):
    index, value = 0, 0

    for current in itertools.count():
        # skip first
        if current in (0, 1):
            continue

        if is_prime(current):
            index += 1
            value = current

        if index == number:
            return value


if __name__ == "__main__":
    print(get_prime(10001))
