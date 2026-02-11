def solution(numbers):
    answer = ''
    num_dict={str(k): [] for k in range(10)}
    
    for n in numbers:
        num_dict[str(n)[0]].append(n)

    def custom_key(x: str):
        return x + n*(max_len-len(x)), len(x) if len(x) > 1 and x[1] < x[0] else -len(x) # len(x) > 1: 한 자리수에서 오류 방지
        
    for n in ["9","8","7","6","5","4","3","2","1","0"]:
        if num_dict[n]:
            max_len = len(str(max((num_dict[n]))))
            num_dict[n] = list(map(str, num_dict[n]))
            num_dict[n].sort(key=custom_key, reverse=True)
            for nums in num_dict[n]:
                answer += nums

    return str(int(answer)) # 0000이 아니라 0임