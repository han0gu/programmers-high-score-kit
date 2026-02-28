def solution(clothes): # max 30개, 30종, 20자
    # 1개씩 30종 -> 숫자 엄청 커짐
    from collections import defaultdict
    answer = 0
    types = defaultdict(int)

    for _, c in clothes: # head 2 eye 1
        types[c] += 1
    
    tmp = 1
    for v in types.values():
        tmp *= (v+1)
    answer = tmp - 1
        
    return answer

# 이 밑은 사고 흐름을 복기하기 위해 남겨둔 것.
# 아래 풀이들에 대한 comment 여부는 code assistant의 자율 판단에 맡김.
"""
def solution(clothes): # max 30개, 30종, 20자
    # 168.64ms
    # 2개씩 15종 -> 숫자 엄청 커짐
    # key = 종류
    # 존재성 -> set or value=True
    from itertools import permutations, combinations
    from collections import defaultdict
        
    answer = 0
    
    closet = [t for _, t in clothes]
    types = defaultdict(int)
    for c in closet: # head 2 eye 1
        types[c] += 1
    
    for i in range(1, len(types.keys())+1):
        for combo in combinations(types.values(), i):
            tmp = 1
            for c in combo:
                tmp *= c
            answer += tmp                       
        
    return answer
"""

"""
def solution(clothes): # max 30개, 30종, 20자
    # 1019.10ms
    from collections import defaultdict
    from itertools import combinations
    answer = 0
    
    closet = [t for _, t in clothes]
    types = set(closet)
    
    if len(types) == 1:
        return len(clothes)
    else:
        answer += len(clothes)
    
    for i in range(2, len(types)+1):
        for p in combinations(closet, i):
            if len(set(p)) == i: 
                answer += 1
        
    return answer
"""