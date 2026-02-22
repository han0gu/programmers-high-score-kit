# 문제 풀이

## 🎯 접근 전략
- 모든 순열 생성
- 생성된 각 케이스 별 소수 판별
  - 소수의 정의에 따라 2 ~ sqrt(자신) 까지의 수 중 나눠 떨어지는게 없으면 소수임

---

## ✅ 테스트 결과
- 정답률: 100% (12/12)

---

## ⚠️ Edge Case
- 

---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity
- min:
- max: sigma(r: 1~len(n)): nPr --> O(??)

### Space Complexity
- min: 
- max: 각 permutation연산의 결과를 담아야 하므로 시간복잡도와 동일할 것으로 예상합니다.