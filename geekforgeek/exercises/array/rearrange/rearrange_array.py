# https://www.geeksforgeeks.org/rearrange-array-arri/


def rearrange(data, placeholder=-1):
    """
    time: O(n)
    space: O(n)
    :param data:
    :param placeholder:
    :return:
    """
    arranged = [placeholder] * len(data)

    for index, element in enumerate(data):
        if element != placeholder:
            arranged[element] = element

    return arranged


if __name__ == "__main__":
    assert rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]) == [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
    assert rearrange([19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
                      11, 10, 9, 5, 13, 16, 2, 14, 17, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                               11, 12, 13, 14, 15, 16, 17, 18, 19]
    print("Ok")
