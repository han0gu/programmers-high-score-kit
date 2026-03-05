# 1. sum: {장르: 횟수 합}
# 2. idx: {장르: [고유번호, 횟수]} -> 정렬(key=lamda x:x[2])
# 3. k = len(sum) -> 장르의 수
# 4. (k * 2)개의 곡을 선택해야 함. sum을 통해서 먼저 고를 장르를 구함
# 5. 구하면서 장르에 속한 곡이 하나면 하나만, 횟수가 같다면 인덱스 낮은 순
def solution(genres, plays):
    answer = []
    d_idx = {}
    d_sum = {}
    
    n = len(genres)
    for i in range(n):
        # 1. sum: {장르: 횟수 합}   
        if genres[i] in d_sum:
            d_sum[genres[i]] += plays[i]
        else:
            d_sum[genres[i]] = plays[i]
            
        # 2. idx: {장르: [고유번호, 횟수]}
        if genres[i] in d_idx:
            d_idx[genres[i]].append([i, plays[i]])
        else:
            d_idx[genres[i]] = [[i, plays[i]]]
        
    d_sum = sorted(d_sum.items(), key=lambda x: x[1], reverse=True)             # [('pop', 3100), ('classic', 1450)]
    
    for j in d_idx:
        d_idx[j].sort(key=lambda x: x[1], reverse=True)                         # {'classic': [[3, 800], [0, 500], [2, 150]], 'pop': [[4, 2500], [1, 600]]}
    
    
    for k in range(int(len(d_sum))):
        if len(d_idx[d_sum[k][0]]) == 1:
            answer.append(d_idx[d_sum[k][0]][0][0])
        else:
            answer.append(d_idx[d_sum[k][0]][0][0])
            answer.append(d_idx[d_sum[k][0]][1][0])
    
    return answer

if __name__ == '__main__':
    x = ["classic", "pop", "classic", "classic", "pop"]
    y = [500, 600, 150, 800, 2500]
    print(solution(x, y))