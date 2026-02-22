from typing import List


def solution(numbers: str):
    print("numbers", numbers)  # "0321589"
    answer = 0

    cases = create_all_cases(numbers)

    for c in cases:
        print(f"{c}: {is_prime_number(c)}")
        if is_prime_number(c):
            answer += 1

    return answer


def create_all_cases(numbers: str):
    cases: List[int] = []

    splitted = [int(n) for n in numbers]
    print("splitted", splitted)  # [0,3,2,1,5,8,9]

    print("total cases:", len(cases))
    return cases


def is_prime_number(num: int):
    if num == 1 or num == 2:
        return True

    for div in range(2, num):
        if num % div == 0:
            return False
    return True


numbers = "17"
# numbers = "011"
# numbers = "0321589"

# 단위 테스트
# create_binary_list(numbers)

# 통합 테스트
print("answer:", solution(numbers))
