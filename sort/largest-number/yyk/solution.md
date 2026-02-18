# 문제 풀이

## 🎯 접근 전략
- 문자를 3번곱해서 문자열순으로 소팅, 리버스
- compare 함수기능을 import 해서 기능을 이용하여 문자열 비교 소팅
- from functools import cmp_to_key


---

## ✅ 테스트 결과
- 정답률: 100% (10/10)

---

## ⚠️ Edge Case
- 
testcase 11 통과 못함. 000 
return answer 에서 000인경우 0을 갖도록, str(int(answer)) 로 변경 ---통과
---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity
- min:
- max: 문자열 전체를 비교하며 소팅하고 for문으로 한차례 돎 O(nlogn)

### Space Complexity
- min:
- max: answer 이 필요하므로 O(1)