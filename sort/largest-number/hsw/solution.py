from functools import cmp_to_key


def compare(a: int, b: int):
    return int(str(b) + str(a)) - int(str(a) + str(b))


def solution(numbers):
    reversed = sorted(numbers, key=cmp_to_key(compare))
    result = "".join([str(n) for n in reversed])
    return str(int(result)) if result else result
