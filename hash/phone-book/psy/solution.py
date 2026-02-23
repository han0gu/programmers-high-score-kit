def solution(phone_book):
    from collections import defaultdict
    p_dic=defaultdict(list)
    
    shortest=20
    longest=0
    for p in phone_book:
        if len(p) < shortest: shortest = len(p)
        if len(p) > longest: longest = len(p)

    if shortest==longest: return True
    
    for p in phone_book:
        if p in p_dic.keys():
            return False
        for i in range(shortest, len(p)+1):
            p_dic[p[:i]].append(p)
            
            
    for p in phone_book:
        if p_dic[p] and len(p_dic[p]) > 1:
            return False

    return True
    
#    테스트 3 〉	통과 (23.41ms, 30MB)
#    테스트 4 〉	통과 (290.65ms, 84.2MB)
#============ TEST CASE ===========
tc = {
    "case3": ["001", "01", "1"], # critical
    "case4": ["222", "23", "22", "2"], # critical
    "case5": ["222", "2222", "22", "2"],
    "case1": ["1", "23", "234"],
    "case2": ["1", "2", "23"],
    "case5": ["12", "13", "1"],
}
for k, v in tc.items():
    print(sorted(v))
    print(solution(v))
    
# 테스트 3 〉	통과 (21.17ms, 30MB)
# 테스트 4 〉	통과 (325.40ms, 84.2MB)
"""저장용 이전 풀이
def solution(phone_book):
    from collections import defaultdict

    p_dic=defaultdict(list)

    for p in phone_book:
        for i in range(1, len(p)+1):
            p_dic[p[:i]].append(p)
        if p in p_dic.keys():
            return False
            
    for p in phone_book:
        if p_dic[p] and len(p_dic[p]) > 1:
            return False

    return True
"""