# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

import random


def solution1(data):
    """
    time: ?
    space: ?
    :param data:
    :return:
    """
    return data[::-1]


def solution2(data):
    """
    time: ?
    space: ?
    :param data:
    :return:
    """
    return reversed(data)


def solution3(data):
    """
    time: O(n)
    space: O(1)
    :param data:
    :return:
    """
    data_length = len(data)
    for index, _ in enumerate(data):
        yield data[data_length - 1 - index]


def solution4(data):
    """
    Generate a new array
    Time: O(n)
    :param data:
    :return:
    """
    data_length = len(data)
    reverted = [None] * data_length

    for left_index, element in enumerate(data):
        right_index = data_length - 1 - left_index

        if right_index == left_index:
            reverted[left_index] = element
            break
        elif left_index > right_index:
            break
        else:
            reverted[right_index] = element
            reverted[left_index] = data[data_length - 1 - left_index]

    return reverted


def solution5(data):
    """
    Swap in place
    Time: O(n)
    :param data:
    :return:
    """
    data_length = len(data)

    for left_index, element in enumerate(data):
        right_index = data_length - 1 - left_index

        if right_index == left_index:
            data[left_index] = element
            break
        elif left_index > right_index:
            break
        else:
            right_element = data[data_length - 1 - left_index]
            data[right_index] = element
            data[left_index] = right_element

    return data


def reverse(data):
    sol = random.choice([
        solution1,
        solution2,
        solution3,
        solution4,
        solution5
    ])

    return list(sol(data))


if __name__ == "__main__":
    assert reverse([2, 3, 4, 2]) == [2, 4, 3, 2]
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([4, 5, 1, 2]) == [2, 1, 5, 4]
    print("Ok")
