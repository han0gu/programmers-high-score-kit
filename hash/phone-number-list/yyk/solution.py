def solution(phone_book):
    
# 주어진 문자열 소팅, i+1 이 i로 시작하는지!
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        # if phone_book[i+1].startswith(phone_book[i]) is bool or True:
        #     return True
        # print(phone_book)
        # False 만 나오면 나머지는 True 이어야 하므로
        # 다 필요없고, return True
    return True