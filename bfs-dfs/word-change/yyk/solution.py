def solution(begin, target, words):
    if target not in words:
        return 0
    # 타겟이 워드에 없을 때 리턴0 예외처리
    # fst in fst out queue
    queue = [[begin,0]]
    visited = []
    # 큐 빌 때까지 반복
    while len(queue) > 0:
        current = queue.pop(0)
        curr_word = current[0]
        step = current[1]
    # 타겟이 되었다면 리턴    
        if curr_word == target:
            return step
    
    # words 하나씩 돌면서 다음단계로 갈 수 있는지 체크
        for word in words:
            if word not in visited:
                # 한 글자만 다른지 체크
                diff_count = 0
                for i in range(len(curr_word)):
                    if curr_word[i] != word[i]:
                        diff_count +=1
                # 딱 한글자만 다르다면?
                if diff_count == 1:
                    visited.append(word) # 방문처리
                    queue.append([word,step +1]) # 다음 탐색 후보
                    
    return 0
#                 # if words[i][j] == begin[j]:
#                       diff = begin[:j] + words[i][j] + begin[j+1:]
#                 if diff == words[i] and begin != word[i]:
#                     return True
#             return begin = diff
    
    
#     if target in words:
        
                
#     # 하나씩 변경되는 것을 깊이 탐색
#     # 워드 소팅, 문자열.
        
#     answer = sorted(words)
    # return answer


# deque 풀이 예시
# 리스트의 pop(0)은 앞 원소를 꺼낼 때마다 뒤 원소들을 한 칸씩 당겨야 한다.
# BFS처럼 앞에서 꺼내는 연산이 많을 때는 deque의 popleft()가 더 효율적이다.
#
# from collections import deque
#
# def solution_deque(begin, target, words):
#     if target not in words:
#         return 0
#
#     queue = deque([(begin, 0)])
#     visited = set([begin])
#
#     while queue:
#         curr_word, step = queue.popleft()
#
#         if curr_word == target:
#             return step
#
#         for word in words:
#             if word in visited:
#                 continue
#
#             diff_count = 0
#             for i in range(len(curr_word)):
#                 if curr_word[i] != word[i]:
#                     diff_count += 1
#
#             if diff_count == 1:
#                 visited.add(word)
#                 queue.append((word, step + 1))
#
#     return 0


# [v]target이 words에 없으면 0 리턴
# [ ]현재 단어와 후보 단어가 정확히 1글자만 다를 때만 이동 가능 -> 별도 함수로 판별
# [ ]deque를 사용해 begin부터 BFS 탐색 수행 + 단어 방문 배열(words 기준) 사용
# [ ]target을 만나면 현재 변환 횟수 리턴
