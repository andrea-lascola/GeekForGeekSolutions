# https://www.geeksforgeeks.org/microsoft-idc-interview-experience/
import collections


def first_non_reapeating_char(string):
    counter = collections.Counter(string)
    for element in string:
        if counter.get(element) == 1:
            return element


if __name__ == "__main__":
    assert first_non_reapeating_char("aabcbd") == "c"
    assert first_non_reapeating_char("abcbd") == "a"
    assert first_non_reapeating_char("aabbdbd") is None
    print("Ok")
