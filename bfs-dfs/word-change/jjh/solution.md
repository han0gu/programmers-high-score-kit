# 문제 풀이

## 🎯 접근 전략

0. target이 words에 없으면 0 리턴
1. 현재 단어와 후보 단어가 정확히 1글자만 다를 때만 이동 가능 -> 별도 함수로 판별
2. deque를 사용해 begin부터 BFS 탐색 수행 + 단어 방문 배열(words 기준) 사용
3. target을 만나면 현재 변환 횟수 리턴

---

## ✅ 테스트 결과

- 정답률: 5/5

---

## ⚠️ Edge Case

- 단계별 변환할 수 있는 경우가 엄청 많은 경우

---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity

- min:
- max: O(N\*\*2) bfs 2중 반복문(while, for)

### Space Complexity

- min: O(N)
- max: O(N)
