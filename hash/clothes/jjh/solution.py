# 1차 
# from collections import Counter
# # 해시 -> 시간 복잡도: O(1)로 원하는 결과 출력 
# def solution(clothes):
#     answer = 0
#     cnt = Counter(i[1] for i in clothes)            # Counter({'headgear': 2, 'eyewear': 1})
#     digits = list(cnt.values())                     # [2, 1]
#     # print(cnt)
#     # print(digits)
#     if len(digits) == 1:
#         answer += digits[0]
#     else:
#         flag = 1
#         answer += sum(digits)
#         for i in digits:
#             flag *= i
#         answer += flag
#     return answer
        

# # x = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],["blue_sunglasses2", "eyewear"] ,["green_turban", "headgear"],["yellow_hat1", "headgear"],["green_turban1", "headgear"], ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# # x = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# x = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# print(solution(x))

# 2차
from collections import Counter
import math

def solution(clothes):
    answer = 0
    cnt = Counter(i[1] for i in clothes)            # Counter({'headgear': 2, 'eyewear': 1})
    digits = list(cnt.values())
    if len(digits) == 1:
        answer += digits[0]
    else:
        for j in range(len(digits)):
            digits[j] += 1
        answer = math.prod(digits) - 1
    return answer
        

x = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],["blue_sunglasses2", "eyewear"] ,["green_turban", "headgear"],["yellow_hat1", "headgear"],["green_turban1", "headgear"], ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# x = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# x = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(x))