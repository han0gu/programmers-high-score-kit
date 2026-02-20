from collections import Counter

# 아래 소수 판별 함수는 ,,, 나무위키 참고했습니다... 다른 방식으로도 구현해보겠습니다..!
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    # 카운터 객체(딕셔너리) 생성 -> 각 숫자의 갯수 저장
    cnt = Counter(numbers)
    # 카운터 딕셔너리의 키를 요소로 갖는 리스트 생성(중복처리 할 필요 없음)
    digits = list(cnt.keys())
    # 백트래킹 과정 담을 리스트
    path = []
    # 백트래킹 최대 횟수
    n = len(numbers)

    # 모든 로직 순환 후, 남는 결과 리스트 -> numbers를 사용해서 만들 수 있는 모든 경우 저장
    out = []

    # 백트래킹 함수
    def dfs():
        # 백트래킹 결과가 있고, 0이 아니면 결과 저장
        if path:
            val = int("".join(path))
            if val != 0:
                out.append(val)

        # 기저 조건(종료 조건)
        if len(path) == n:
            return

        # 숫자 뽑기
        for char in digits:
            # 뽑기 전, 갯수 확인
            if cnt[char] == 0:
                continue
            # 맨 앞 0 방지 로직
            if not path and char =='0':
                continue

            # 뽑은 숫자 백트래킹 리스트에 추가
            path.append(char)
            # 해당 숫자 갯수 차감
            cnt[char] -= 1

            # 백트래킹
            dfs()

            # 재귀에서 나왔을 때, 방금 사용한 숫자 돌려놓기
            path.pop()
            cnt[char] += 1
    
    dfs()

    for candidate in out:
        if is_prime(candidate):
            answer += 1

    return answer