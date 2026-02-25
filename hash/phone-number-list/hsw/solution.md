# 문제 풀이

## 🎯 접근 전략

- 두 수를 선택한 후, 순서를 바꿔가며 접두어 여부를 확인한다.

### try 1
- 접두어 여부 확인 함수
    ```python
    def is_dup(num1: str, num2: str):
        return num2.startswith(num1) or num1.startswith(num2)
    ```
- 테스트 결과
    - 성능 테스트 통과 실패
        ![alt text](try1.png)

### try 2
- 접두어 여부 확인 함수
    ```python
    def is_dup(num1: str, num2: str):
        len1: int = len(num1)
        len2: int = len(num2)

        if len1 < len2:
            return num2.startswith(num1)
        elif len1 > len2:
            return num1.startswith(num2)
        else:
            return num1 == num2
    ```
- 테스트 결과
    - 비교 횟수 감소를 통해 성능 개선 시도하였으나 여전히 성능 테스트 통과 실패
        ![alt text](try2.png)

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