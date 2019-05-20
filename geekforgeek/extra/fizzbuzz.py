'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"
'''
from typing import List


def fizzbuzz(array: List[int]):

    for element in array:
        if element % 3 == 0 and element % 5 == 0:
            print("FizzBuzz")
        elif element % 3 == 0:
            print("Fizz")
        elif element % 5 == 0:
            print("Buzz")
        else:
            print(element)


if __name__ == '__main__':
    fizzbuzz([x for x in range(100)])
