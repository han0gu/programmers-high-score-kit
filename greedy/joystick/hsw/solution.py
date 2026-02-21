import re


def solution(name: str):
    answer = 0

    pattern = r"[^A]"
    matches = re.search(pattern, name)
    if not matches:
        return 0

    answer += count_left_right(name)

    for s in name:
        c = count_up_down(s)
        # print("c", c)
        answer += c

    return answer


def count_left_right(name: str):
    name = name[1:]  # 첫 글자 제외
    pattern = r"[^A]"

    matches_right = list(re.finditer(pattern, name))
    # print("matches_right", matches_right)
    right = matches_right[-1].end()
    # print("right:", right)

    matches_left = list(re.finditer(pattern, name[::-1]))
    # print("matches_left", matches_left)
    left = matches_left[-1].end()
    # print("left:", left)

    return min(left, right)


def count_up_down(target_alphabet: str) -> int:
    total_alphabet_count = 26
    criteria_ord = ord("A")
    target_alphabet_ord = ord(target_alphabet)
    gap = target_alphabet_ord - criteria_ord

    # 올라가야하는 경우
    if gap <= total_alphabet_count / 2:
        return gap
    # 내려가야하는 경우
    else:
        return abs(total_alphabet_count - gap)


# count_up_down test
# print(count_up_down("J"))
# print(count_up_down("Z"))
# print(count_up_down("Y"))
# print(count_up_down("X"))
# print(count_up_down("U"))
# print()

# count_left_right test
# right: 3,12
# left: 8, 17
# print(solution("AAACAAAAAAAATAAAAAAA"))

# edge test
# print(solution("AAAAAA"))

# solution test
# print(solution("JAZ"))
# print(solution("JEROEN"))
