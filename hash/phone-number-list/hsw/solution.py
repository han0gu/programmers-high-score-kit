def solution(phone_book):
    for idx in range(len(phone_book) - 1):
        num1 = phone_book[idx]

        for jdx in range(idx + 1, len(phone_book)):
            num2 = phone_book[jdx]

            # print(f"{num1}, {num2}: {is_dup(num1, num2)}")
            if is_dup(num1, num2):
                return False

    return True


def is_dup(num1: str, num2: str):
    return num2.startswith(num1) or num1.startswith(num2)
