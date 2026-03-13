def solution(numbers):
    from itertools import permutations
    answer = 0
    # 모든 조합 만들기
    sep_num = [n for n in numbers]
    # print(sep_num)
    case = []
    for i in range(1, len(numbers)+1):
        for perm in [*permutations(sep_num, i)]:
            case.append(int(''.join(perm)))
    case = list(set(case))
    print(case)
    
    # 소수 판별
    for c in case:
        if c == 1 or c == 0: continue
        
        isPrime = True
        for i in range(2, int((c**0.5))+1):
            if c % i == 0:
                isPrime = False
                break
        if isPrime: answer += 1
    
    return answer

test_case={
    "case1": "17",
    "case2": "011",
}
for k, v in test_case.items():
    print(solution(v))
# =======================================================    
# Gemini code refactoring recommendation:
# =======================================================
# def solution(numbers):
#     from itertools import permutations
    
#     # 1. 모든 숫자 조합 생성 (Set Comprehension)
#     uniques = {int(''.join(p)) for i in range(1, len(numbers) + 1) 
#                for p in permutations(numbers, i)}
    
#     # 2. 소수 판별 (Generator + any)
#     def is_prime(n):
#         if n < 2: return False
#         return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))
    
#     # 3. 결과 카운트 (Boolean의 합은 True의 개수임을 활용)
#     return sum(1 for n in uniques if is_prime(n))