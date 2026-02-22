from itertools import permutations


def solution(numbers: str):
    all_cases = create_all_cases(numbers)

    primes = {c for c in all_cases if is_prime_number(c)}

    return len(primes)


def create_all_cases(numbers: str) -> set:
    all_cases: set = set()

    for i in range(len(numbers)):
        cases = permutations(numbers, i + 1)

        for case in cases:
            converted = int("".join(case))  # (0,1,1) -> "011" -> 11
            all_cases.add(converted)

    return all_cases


def is_prime_number(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True

    for div in range(2, num):
        if num % div == 0:
            return False
    return True
