# https://www.geeksforgeeks.org/split-array-add-first-part-end/


def split_array(data, split_index):
    """
    time: O(n)
    space: O(1)
    :param data:
    :param split_index:
    :return:
    """
    for index, element in enumerate(data):
        yield data[(index + split_index) % len(data)]


if __name__ == "__main__":
    assert list(split_array([1, 2, 4, 5, 3], 1)) == [2, 4, 5, 3, 1]
    print("Ok")
