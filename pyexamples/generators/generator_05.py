import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_prime(n):
    """the traditional version"""
    result = []
    for i in range(1, n):
        if is_prime(i):
            result.append(i)

    return result


def gen_prime(n):
    """the generator version"""
    for i in range(1, n):
        if is_prime(i):
            yield i


print("\ntraditional version")
print(get_prime(20))

print("\ngenerator version with for loop")
for i in gen_prime(20):
    print(i)

print("\ngenerator version with list constructor")
print(list(gen_prime(20)))

