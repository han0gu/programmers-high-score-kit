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