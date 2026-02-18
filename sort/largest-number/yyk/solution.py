def solution(numbers):
    answer = ''
    # numbers = str(numbers)
    # numbers = sorted(numbers)
    # # numbers = int(numbers)
    # # numbers = reversed(numbers)
    # numbers = numbers[::-1]
    # return numbers
    # for i in range(len(numbers)) :
        
    #먼저 소팅?
    #첫자리수가 큰 것이 먼저온다. answer += numbers[i]
    #첫자리수가 같은데 뒷자리 수가 없다면, 인덱스 빠른것이 먼저 온다.
    #첫자리수가 같으면 두번째자리수가 큰 것이 먼저온다.
    #두번째자리수가 같으면 세번째 자리수가 큰 것이 먼저온다.
    #세번째 자리수가 같으면 마지막 자리수가 큰 것이 먼저온다.
    #더이상 비교할 자리수가 없으면 다음으로
    
    #소팅, 문자열사전순으로, 리버스. --> 그대로 answer에 넣으면 됨
    #가능한가, 가능, 그러나 , [,] 모두 문자로 인식을 해버림
    #"]","[","6","2","1","0",",",","," "," "
    #이방법 x, 인덱스의 0번째 문자열을 꺼내서 순서대로 나열 + 0번째 같으면 원래 순으로 소팅
    # 람다 리버스!
    # numbers = sorted(numbers, key= lambda x : (str(x)[0],x))
    # numbers = reversed(numbers)  #TypeError: Object of type list_reverseiterator is not JSON serializable
    
    # numbers = numbers[::-1]
    #테스트2 303-->330되야함
    # numbers = sorted(numbers, key= str, reverse = True)
    # numbers = sorted(numbers, key= lambda x: (str(x)[0],len(str(x)),x) ,reverse = True)
    numbers = sorted(numbers, key= lambda x: str(x)*3 ,reverse = True)
    # return numbers
    # return numbers   #[3,30,34,5,9] ->리버스하면  [9,5,34,30,3]
    # i = 0
    for i in range(len(numbers)):
        answer += str(numbers[i]) #answer 는 문자열받는데, numbers는 정수값이라 못받아서 문자변환
    
    if int(answer) == 0 : return 0
    if len(answer) != 0 : return answer

    # return answer





"""method 1"""

def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key= lambda x: str(x)*3 ,reverse = True)
    
    for i in range(len(numbers)):
        answer += str(numbers[i])
        
    if int(answer) == 0 : return str(int(answer))
    if len(answer) != 0 : return str(int(answer))


"""method 2"""
from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    def compare(a,b):
        if str(a)+str(b) > str(b)+str(a): #ab가 ba 보다 크면 a가 앞
            return -1
        else:
            return 1


    numbers = sorted(numbers, key = cmp_to_key(compare))
    
    for i in range(len(numbers)):
        answer += str(numbers[i])
    if answer == 0 : return str(int(answer))
    if len(answer) != 0 : return str(int(answer))

#엣지케이스 000 일때!
#정수 변환 후 문자열 변환하여 0을 answer가 갖도록함