from collections import Counter
from itertools import combinations


def solution(clothes):
    answer = 0

    if len(clothes) == 1:
        return 1

    category_counter = Counter([category for name, category in clothes])

    d = dict(category_counter)  # { 'headgear': 3, 'eyewear': 2, 'face': 5, 'top': 4 }
    print(f"d: {d}\n")
    values = list(d.values())

    for i in range(len(values) + 1):
        combs = combinations(values, i + 1)

        for c in combs:
            print(f"{i + 1}가지 아이템 선택: {c} -> {calculate(c)}")
            answer += calculate(c)
        print()

    return answer


def calculate(combination: tuple):
    sum = 1
    for num in combination:
        sum *= num
    return sum


clothes = [
    ["a", "headgear"],
    ["b", "headgear"],
    ["j", "headgear"],
    ["c", "eyewear"],
    ["d", "eyewear"],
    ["e", "face"],
    ["f", "face"],
    ["g", "face"],
    ["h", "face"],
    ["i", "face"],
    ["k", "top"],
    ["l", "top"],
    ["m", "top"],
    ["n", "top"],
]

# clothes = [
#     ["yellow_hat", "headgear"],
#     ["blue_sunglasses", "eyewear"],
#     ["green_turban", "headgear"],
# ]

print(f"합계: {solution(clothes)}")
