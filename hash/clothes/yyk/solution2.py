from itertools import product

def solution(clothes):
    
#     # [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

#     # 리스트 안에 리스트형태, 그룹지어 매핑

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
#         # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
#         # 같은 부위 의상끼리 그룹화 했음.
#         # 다음은, 딕셔너리 조합

    
#         # 값이 가변적인 딕셔너리를 함수인자로 받으려면 ** 붙여야 한다)


#         # 키의 값을 0 또는 1개씩 가져오는 조합
#         # combination 조합
#         # 서로 다른 n개의 원소를 가지는 어떤 집합 s에서 k개를 선택해 조를 만드는 것
#         # product set 곱집합 
#         # A1,A2를 임의의 집합이라 할 때, a∈A1인 원소 a를 첫째 원소로 하고, b∈A2인 b를 둘째 원소로 하는 모든 순서쌍(a,b)의 집합을 A1과 A2의 곱집합이라 하고 A1×A2로 나타낸다
    def product_dict(**kwargs):
        sets = kwargs.values()
        for ways in product(*sets): 
            # * : 언패킹, 리스트나 튜플 앞에 붙는데, 자료구조를 풀어서 인자로 전달하는 역할 
            return list(ways)
    
    
    def total_ways(clothes):
        group = mk_grouped_dict(clothes)
        answer = product_dict(**group)
        return len(answer)

    return total_ways(clothes)
