# 의상 (프로그래머스 42578)

## 문제 설명
코니는 매일 다른 옷을 조합하여 입는 것을 좋아합니다.

각 종류별로 최대 1가지 의상만 착용할 수 있습니다.  
일부 의상이 겹치더라도, 다른 의상이 다르거나 추가된 경우 서로 다른 조합으로 계산합니다.  
하루에 최소 한 개의 의상은 반드시 착용합니다.

코니가 가진 의상들이 담긴 2차원 배열 `clothes`가 주어질 때,
서로 다른 옷의 조합의 수를 return 하도록 `solution` 함수를 작성하세요.

---

## 제한사항
- `clothes`의 각 행은 `[의상의 이름, 의상의 종류]` 형태입니다.
- 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 없습니다.
- 모든 원소는 문자열입니다.
- 문자열 길이는 1 이상 20 이하이며, 알파벳 소문자 또는 `_`로만 구성됩니다.

---

## 입출력 예

| clothes | return |
|---|---:|
| `[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]` | 5 |
| `[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]` | 3 |

---

## 입출력 예 설명

### 예제 1
headgear: yellow_hat, green_turban  
eyewear: blue_sunglasses  

가능한 조합 (총 5가지):

1. yellow_hat
2. green_turban
3. blue_sunglasses
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses

### 예제 2
face: crow_mask, blue_sunglasses, smoky_makeup  

가능한 조합 (총 3가지):

1. crow_mask
2. blue_sunglasses
3. smoky_makeup

---

## 출처

https://school.programmers.co.kr/learn/courses/30/lessons/42578