# 0. target이 words에 없으면 0 리턴
# 1. 현재 단어와 후보 단어가 정확히 1글자만 다를 때만 이동 가능 -> 별도 함수로 판별
# 2. deque를 사용해 begin부터 BFS 탐색 수행 + 단어 방문 배열(words 기준) 사용
# 3. target을 만나면 현재 변환 횟수 리턴
from collections import deque

def word_diff(word, candi):
    n = len(word)
    diff = 0
    
    for i in range(n):
        if word[i] != candi[i]:
            diff += 1
        if diff > 1:
            return 0
    if diff == 1:
        return 1
    return 0

def solution(begin, target, words):
    n = len(words)
    
    # 0) words 안에 target이 없으면 0 리턴
    if not target in words:
        return 0
    
    # 1-3) words 안에 target이 존재
    q = deque()
    v = [0] * n
    q.append((begin, 0))
    
    # bfs
    while q:
        curr, cnt = q.popleft()
        if curr == target:
            return cnt
        for i in range(n):
            if not v[i] and word_diff(curr, words[i]): # 방문 안 했고, 차이가 딱 1인 경우
                v[i] = 1
                q.append((words[i], cnt + 1))
    return 0

if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))