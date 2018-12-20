# https://www.hackerrank.com/challenges/diagonal-difference/problem
from typing import List


def diagonalDifference(arr: List[int]):
    pass


if __name__ == "__main__":
    # assert diagonalDifference([])

    arr = []
    n = 10

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
