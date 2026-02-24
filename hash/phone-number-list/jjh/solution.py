# 1차 풀이
# def solution(phone_book):
#     answer = True
#     n = len(phone_book)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if phone_book[i] in phone_book[j]:
#                 answer = False
#                 break
            
#     return answer

# 2차 풀이
def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    i = 0
    while i + 1 < n:
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
        i += 1

    return answer

# x = ["123","456","789"]
# print(solution(x))