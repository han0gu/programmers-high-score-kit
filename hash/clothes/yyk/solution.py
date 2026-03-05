from itertools import product

def solution(clothes):
    
    
    # [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

    # 리스트 안에 리스트형태, 그룹지어 매핑

    def mk_grouped_dict(clothes):
        mapping = {}
        for item in clothes:
            key = item[1] #부위를 키로
            value = item[0] #의상을 밸류로
            if key in mapping:
                mapping[key].append(value)

            else: 
                mapping[key] = [value]

        return mapping
    
    
    def total_combinations(clothes):
        answer = 1
        for i in mk_grouped_dict(clothes).keys():
            clothes_count = len(mk_grouped_dict(clothes)[i])
            answer *= (clothes_count + 1)
        return answer - 1
        #딕셔너리 키의 값을 +1 한것들을 모두 곱 -1
        # +1은 안입는 경우를 포함하기 위함
        # 곱셈은 모든 경우의 수를 구하기 위함
        # -1은 모두 안입는 경우를 제외하기 위함
    return total_combinations(clothes)
