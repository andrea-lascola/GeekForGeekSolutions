# https://www.geeksforgeeks.org/find-second-largest-element-array/

from typing import List


def second_maximum(arr: List[int]):
    # Time: O(nlogn)
    # Space: O(n)

    unique = list(set(arr))
    if len(unique) < 2:
        return None
    return sorted(unique)[-2]


def second_maximum_best(arr: List[int]):
    # Time: O(n)

    if not arr:
        return None

    maximum, second = arr[0], None

    for index, element in enumerate(arr):
        if index == 0:
            continue

        if element > maximum:
            second = maximum
            maximum = element
        elif not second or element >= second:
            second = element
    return second


if __name__ == "__main__":
    assert second_maximum_best([3, 5, 2, 1, 7, 9, 6]) == 7
    assert second_maximum_best([1, 5, 2, 1, 5]) == 5
    assert second_maximum_best([12, 35, 1, 10, 34, 1]) == 34
    assert second_maximum_best([10, 5, 1]) == 5

    assert second_maximum_best([10, 10, 10]) is 10

    assert second_maximum_best([10]) is None
    assert second_maximum_best([]) is None
