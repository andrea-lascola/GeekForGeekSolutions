# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def smallest_divisible(limit: int):
    index = 1
    while True:
        if all([index % (x + 1) == 0 for x in range(limit)]):
            return index
        index += 1


if __name__ == "__main__":
    assert smallest_divisible(10) == 2520

    print(smallest_divisible(20))
