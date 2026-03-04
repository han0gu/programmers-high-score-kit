
def solution(numbers):
    # 주어진 문자열로 만들 수 있는 조합을 나열하기 - itertools permutations
        # result = list(permutations(iterable, r = None))
        # r 지정하지 않으면 nunbers 길이 만큼 데이터 뽑아 모든 경우 계산 나열,Tuple  
        # [(a,b,c), (a,c,b), (b,c,a)] x  -> 0,1,10,11,101,.. 길이 1부터 전부 생성해야함
    from itertools import permutations
    result = []
    for i in range(1, len(numbers)+1): #길이 1부터의 조합 나열
        # for p in permutations(numbers, i):
        result += [p for p in permutations(numbers, i)] # [(a,b,c), (a,c,b)]
    result = [''.join(permutated) for permutated in result] #['011','010']
    result = [int(string) for string in result] # 리스트컴프리헨션 써서 정수변환
    result = list(set(result)) # set 함수로 중복 제거
    # if 1 in result:
    #     result.remove(0)
    # if 0 in result:
    #     result.remove(1) # 0,1 제거
    result = [e for e in result if e >1] 
    print(result)
    # 1과 자기자신으로만 나누어 떨어지는지 확인 -> 소수만 골라서 담기 prime
        # 소수의 규칙을 이용해서 result에서 뺄 것임
    """
        에라토스테네스의 체
            규칙: 어떤 수 p가 소수라면 2p,3p,4p 배수들은 절대 소수가 아니다
    """ 
        # 1부터 N까지 모든 소수를 찾을 때, 소수를 만날 때마다 그 배수를 빼면
        # 남은 len(result) 가 소수 갯수임
        # 소수 : 2,3,5,7,11,13,17,19,23,...,101,...
        # 2를 제외한 2의 배수 삭제,3을 제외한 3의 배수 삭제, 
        # 5를 제외한 5의 배수 삭제, 7을 제외한 7의 배수 삭제
    result = [x for x in result if x == 2 or x % 2 != 0]
    result = [x for x in result if x == 3 or x % 3 != 0]
    result = [x for x in result if x == 5 or x % 5 != 0]
    result = [x for x in result if x == 7 or x % 7 != 0]
    
        # 2,3,5,7 10 미만의 소수의 배수를 제거하면 소수만 남을 것임
        
#가독성, 익스텐션 적용하기, 주석지우는 등
    
       
    return len(result)





from itertools import permutations
result = []
def solution(numbers):
        
    for i in range(1, len(numbers)+1): #길이 1부터의 조합 나열
        result += [p for p in permutations(numbers, i)] # [(a,b,c), (a,c,b)]
        
    result = [''.join(permutated) for permutated in result] #['011','010']
    result = [int(string) for string in result] # 리스트컴프리헨션 써서 정수변환
    result = list(set(result)) # set 함수로 중복 제거
    
    result = [e for e in result if e >1] 
    return result

def prime(result):  #에라토스테네스의 체
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
    
result = [x for x in result if prime(x)]