# 문제 풀이

## 🎯 접근 전략
- sorted + custom compare function

---

## ⚠️ Edge Case
- 맨 앞 자리가 0인 경우
  - 문자열 -> 숫자 변환으로 해결

---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity
- 가정:
  - n = len(numbers)
  - Python이 Timsort 알고리즘을 이용하여 list를 정렬
- min: 
  - 이미 모든 원소가 정렬된 상태일 때
  - O(n)
- max: 
  - 어느 구간도 정렬되지 않은 상태일 때
  - O(n logn)
- average:
  - O(n logn)

### Space Complexity
- 가정:
  - n = len(numbers)
- min: 
  - O(n)
- max: 
  - O(n)