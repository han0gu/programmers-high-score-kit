def solution(name):
    from copy import deepcopy # visited를 깊은복사 하기 위함
    answer = 0    # len = 1 ~ 20
    visited=[False] * len(name)    
    # 개별 알파벳의 목표 알파벳과의 거리 합산
    visited[0] = True
    for i, c in enumerate(name):
        if c == 'A': 
            visited[i] = True
            continue
        if c <= 'N': 
            answer += ord(c) - ord('A')
        else:
            answer += (26 - (ord(c) - ord('A')))
    
    # 1글자 / A로만 된 문자열 처리
    if len(name) == 1 or answer == 0: return answer
    
    # [백트래킹 알고리즘]
    # 상태 공간을 표현하는 슬라이딩 윈도우를 위한 윈도우 생성 (방향을 꺾는 행위는 최대 1회만 허용됨)
    slide = '0'*len(name) + '1'*len(name) + '0'*(len(name))
    shortest = len(name)-1 # 이동거리 최솟값의 초기 설정
    
    for i in range(len(slide)-len(name)):
        watching = slide[i:i+len(name)]
        # print(watching)
        tmp_visited = deepcopy(visited)
        pos = 0 # init position
        dist = 0 # sum of distance
        
        for w in watching:
            if w == '1': # clockwise
                # print("if")
                for idx in range(pos+1, pos+len(name)):
                    # print("idx:", idx)
                    if not tmp_visited[min(idx, idx % len(name))]: # 해당 방향의 최초 not A 문자 탐지
                        dist += (idx - pos)
                        # print("dist:", dist)
                        pos = min(idx, idx % len(name))
                        tmp_visited[pos] = True
                        break
                if dist > shortest: break # pruning
            
            else: # counter clockwise
                # print("else")
                for idx in range(pos-1, pos-len(name), -1):
                    # print("idx:", idx)
                    if not tmp_visited[max(idx, idx % len(name))]: # 해당 방향의 최초 not A 문자 탐지
                        dist += (pos - idx)
                        # print("dist:", dist)
                        pos = max(idx, idx % len(name))
                        tmp_visited[pos] = True
                        break
                if dist > shortest: break # pruning
        if dist < shortest:
            shortest = dist
        
                        
    # print(answer, shortest)
        
    return (answer + shortest)

# ================< 테스트 >================
pool = [
    # "JEROEN",
    # "JAN",
    # "AAA",
    # "JANAN",
    # "ZZZ",
    # "Z",
    # "NNN",
    "ABBBAAAAABB"
]
for p in pool:
    print(p)
    print(f"{p}: {solution(p)}")
