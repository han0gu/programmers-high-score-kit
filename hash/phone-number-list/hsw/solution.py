def solution(phone_book):
    for idx in range(len(phone_book) - 1):
        num1 = phone_book[idx]

        for jdx in range(idx + 1, len(phone_book)):
            num2 = phone_book[jdx]

            print(f"{num1}, {num2}: {is_dup(num1, num2)}")
            if is_dup(num1, num2):
                return False

    return True


def is_dup(num1: str, num2: str):
    len1: int = len(num1)
    len2: int = len(num2)

    if len1 < len2:
        return num2.startswith(num1)
    elif len1 > len2:
        return num1.startswith(num2)
    else:
        return num1 == num2


phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)
