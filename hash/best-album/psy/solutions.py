def solution(genres, plays):
    from collections import defaultdict
    cnt = defaultdict(int)
    id = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        cnt[g] += p # 장르별 재생 합계
        id[g].append((p, i)) # (재생횟수, 고유번호)

    gen = sorted(list(cnt.keys()), key= lambda x: cnt[x], reverse=True)
    ans = []
    for g in gen:
        if len(id[g]) < 2:
            ans.append(id[g][0][1])
            continue
        id[g].sort(key=lambda x: (x[0], -x[1]), reverse=True) # -x[1]: 재생 횟수 역순 정렬하되 id는 오름차순 유지하기 위한 트릭(?)
        ans.append(id[g][0][1])
        ans.append(id[g][1][1])
    
    return ans

# 아래는 Edge Case 체크용. 코드 리뷰 시, 아래의 코드는 solution 함수와 무관함을 알림.
test = {
    "c1": [["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 1, 3, 0]], # 기존
    "c2": [["jazz", "pop", "pop"], [150, 800, 2500], [2, 1, 0]], # 1개 있는 장르 포함
    "c3": [["jazz", "pop"], [150, 800], [1, 0]], # 1개 있는 장르만
    "c4": [["jazz", "pop", "jazz", "pop"], [150, 800, 150, 800], [1, 3, 0, 2]], # 장르 내 재생횟수 동일
}
print(solution(test["c4"][0], test["c4"][1]))