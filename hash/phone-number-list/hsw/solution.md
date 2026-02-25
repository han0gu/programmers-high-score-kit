# 문제 풀이

## 🎯 접근 전략

- 두 수를 선택한 후, 순서를 바꿔가며 접두어 여부를 확인한다.
- 테스트 결과
    ![alt text](image.png)

---

## ⚠️ Edge Case

- 

---

## 🕰️ 시간 / 공간 복잡도

### Time Complexity

- min:
    - O(1): 첫번째 숫자가 두번째 숫자의 접두어인 경우
- max:
    - O(n<sup>2</sup>): 2중 배열을 끝까지 탐색한 경우
- average:
    - O(n<sup>2</sup>)

### Space Complexity

- min:
    - O(n): `phone_book`의 길이에 비례
- max:
    - O(n): `phone_book`의 길이에 비례
- average:
    - O(n): `phone_book`의 길이에 비례

---

## 🗣️ 마무리

- 내가 느끼는 문제 난이도: 3
    - 기본적인 접근 전략을 떠올리는 것은 쉽다.
    - 성능 개선 방법이 즉시 떠오르지는 않았다.