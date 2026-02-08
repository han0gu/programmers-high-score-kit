# 문제 풀이

## 🎯 접근 전략
- sorted + custom compare function
  ![alt text](image.png)

---

## ⚠️ Edge Case
- 맨 앞 자리가 0인 경우

---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity
- 가정
  - n = len(numbers)
  - Python이 Timsort 알고리즘을 이용하여 list를 정렬
- min: O(log n)
- max: O(log n)

### Space Complexity
- 가정
  - n = len(numbers)
- min: O(n)
- max: O(n)