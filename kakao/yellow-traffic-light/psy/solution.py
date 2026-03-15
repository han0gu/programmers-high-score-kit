from collections import defaultdict
import math
# 정수론 문제 (모듈러)
def solution(signals):
    # 전부 노랑 -> 정전
    # 시간: 1초부터 시작
    # 최초 정전 시각 return, 그런 일 없으면 -1
    # 3초 <= 1 사이클 <= 20초 
    # 평행선이면 -1이겠지? / 주가는 동일한데 겹치는 구간이 없는 경우? 
    # 각 신호는 최소 1초, 최대 18초
    # 신호등은 2 ~ 5개
    answer = -1
    # [1사이클 주기, 첫 노랑불 타이밍, 노랑불 지속 시간] -> 시작과 끝(시작+지속시간)은 알 수 있음
    # 최소공배수 문제인가? --> 모듈러 정수론 문제
    pattern = defaultdict(list)
    for i, s in enumerate(signals):
        pattern[i] = [1+s[0], s[0]+s[1], sum(s)] # 시작, 끝, 주기
        
    max_start = max(v[0] for v in pattern.values())
    min_end = min(v[1] for v in pattern.values())
    
    # -1 이 답인 경우 (동주기, 겹치는 시간 없음)
    if len({v[2] for v in pattern.values()}) == 1:
        if max_start > min_end:
            return -1
        
    # 일정 주기로 점멸하는 불빛 문제로 생각
    # 시간 s에 최초로 켜진 상태이고 주기 c인 경우 -> 임의의 시간 t에 대해  t % c == s 일 때만 켜져 있음 ( s === t mod c )
    # 시간 t에 노란불일 조건: start <= t % cycle <= end
    
    cycles = [v[2] for v in pattern.values()]
    total_lcm = cycles[0] # 프로그래머스 IDE가 math.lcm을 지원하지 않음
    for i in range(1, len(cycles)): # lcm(a, b) == (a * b) / gcd(a, b)
        a, b = total_lcm, cycles[i]
        total_lcm = (a * b) // math.gcd(a, b)
        
    for t in range(max_start, max_start + total_lcm): # 이게 정말 '타이트하게' 다 잡아내는 범위일까?
        cnt = 0 # 뭔가 더 fancy한 방법이 있을 것 같은데...
        for start, end, cycle in pattern.values():
            if start <= (t % cycle) <= end:
                cnt += 1
        if cnt == len(signals):
            return t
    
    return answer
# test case code: Don't Review Under This Line
test = {
    't1': [[2, 1, 2], [5, 1, 1]],
    't2': [[2, 3, 2], [3, 1, 3], [2, 1, 1]],
    't3': [[3, 3, 3], [5, 4, 2], [2, 1, 2]],
    't4': [[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]],
    't5': [[1, 3, 3], [2, 3, 2], [3, 3, 1]],
}
ans = [13, 11, 193, -1, 4]
for (t, a) in zip(test.values(), ans):
    print(solution(t))
