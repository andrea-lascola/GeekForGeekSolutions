def largest_prime_factor(number: int):
    index = number
    while index >= 1:
        index -= 1
        if number % index == 0:
            if is_prime(index):
                return index


def is_prime(number: int):
    for index in range(number)[2:]:
        if number % index == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(3))
    assert largest_prime_factor(13195) == 29

    print(largest_prime_factor(600851475143))
    # print(largest_prime_factor(600851475143))
