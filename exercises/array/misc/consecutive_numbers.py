# https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/


def is_list_consecutive(data):
    """
    time: O(n)
    space O(n)
    :param data:
    :return:
    """
    before = set()
    after = set()
    result = set()
    for element in data:
        if element in result:
            return False

        if element in before:
            before.remove(element)
        if element in after:
            after.remove(element)

        if element - 1 not in result:
            before.add(element - 1)

        if element + 1 not in result:
            after.add(element + 1)
        result.add(element)

    if all([len(before) == 1,
            len(after) == 1,
            len(result) == len(data)]):
        return True
    return False


if __name__ == "__main__":
    one = [1, 5, 2, 5, 3, 65, 6, 8, 2, 54, 0, 6]
    two = [3, 2, 4, 1, 5, 6]
    three = [3, 2, 4, 1, 5, 7]

    assert is_list_consecutive(one) is False
    assert is_list_consecutive(two) is True
    assert is_list_consecutive(three) is False

    print("Ok")
