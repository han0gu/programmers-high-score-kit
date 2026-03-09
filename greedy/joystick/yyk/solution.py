def solution(name):
    answer = 0
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
    alphabet2 = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet2 = alphabet2[::-1]
    # alphabet = list(alphabet)
    # name = "JEROEN" #return 56
    # name = "JAN" #return 23
    # name = "JAZ" #return 11
    # name = "bbbaaaaaaacfds"
    # 다음알파벳, 커서 오른쪽이동 구현. (마지막위치에서 오른쪽이동시 첫번째문자는 아직) (왼쪽, 아래 구현해야함), (위,아래 구현) 좌 우 해야함 
    joystick = list("A"*len(name))
    i = 0
    
    if name.count('A') == len(name):
        return 0 #AAA,AAAAA,AAAAAAAAAAAA,AAAAAAAAAAAAAAAAA 
    
    while i in range(len(name)):
    
        
                # 상 하
        if name[i] != joystick[i]:
            if alphabet.count((name[i])) == 1:
                answer += alphabet.index((name[i])) #이미 A로 시작이므로 +1 하면 안됨
                joystick[i] = name[i]
            else:
                answer += alphabet2.index((name[i])) + 1
                joystick[i] = name[i]
        if name == ''.join(joystick): # 둘이 같으면 끝 (endpoint)
            break        
                # answer += alphabet.index((name[i])) + 1
                # joystick[i] = name[i]
              
              
              # 좌 우 , 비교, 도움, len(name)으로 나눈 나머지를 인덱스로한 값을 비교, 순환시킴
        left =1
        right =1
        #
        while name[(i +right) % len(name)] == joystick[(i +right) % len(name)]:
            right += 1
            # if right > len(name):
            #     break #AAAAA 무한루프 엣지 endpoint //필요없음, 맨 위에서 끝냄.
           
        while name[(i-left) % len(name)] == joystick[(i-left) % len(name)]:
            left += 1
       
        if right <=left: #오른쪽으로 가는게 왼쪽으로가는것보다 가까우면, 또는 왼쪽 오른쪽 둘다 A가 아니면
            answer += right #오른쪽 클릭만큼 더하고
            i = (i +right) % len(name) #커서위치 갱신
        else:
            answer += left # 왼쪽이 가까우면 왼쪽클릭만큼 더하고
            i = (i-left) % len(name) #커서위치 갱신
            
            
            
            # name[i] == joystick[i]:  # A 일때, A갯수 세고, 뒤로 번호와 앞으로번호 크기차이로 좌우 결정?
            # next_i = i + 1
            # # if name[next_i] == "A":
            # while next_i < len(name) and name[next_i] == "A":
            #     next_i += 1
            #     if next_i == len(name):
            #         break
            #     # if name[next_i] != joystick[next_i]: 
                    
                    
            #     #좌우 이동? 선택을 어떻게 하지,---- min((next_i - i), (len(name)(최대20) - (i 번째부터 이어진 A갯수 = next_i))
            #     if (next_i - i) > (len(name) - next_i + i):
            #         answer += (len(name) - next_i + i)
            #         i -= (len(name) - next_i + i)
                    
            #         if name[i] != joystick[i]:
            #             if alphabet.count((name[i])) == 1:
            #                 answer += alphabet.index((name[i])) + 1
            #                 joystick[i] = name[i]
            #             else:
            #                 answer += alphabet2.index((name[i])) + 1
            #                 joystick[i] = name[i]
                    
            #     else:
            #         answer += (next_i - i)
            #         i += (next_i - i)
                    
            #         if name[i] != joystick[i]:
            #             if alphabet.count((name[i])) == 1:
            #                 answer += alphabet.index((name[i])) + 1
            #                 joystick[i] = name[i]
            #             else:
            #                 answer += alphabet2.index((name[i])) + 1
            #                 joystick[i] = name[i]
            #         # answer += 0
                
    
               

                
                
            # return len(name)
        # if name == ''.join(joystick):
        #     return answer
            # else: return 0
        # return alphabet
    return answer

def solution(name):
    answer = 0
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
    alphabet2 = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet2 = alphabet2[::-1]
    
    joystick = list("A"*len(name))
    i = 0
    
    if name.count('A') == len(name):
        return 0 #AAA,AAAAA,AAAAAAAAAAAA,AAAAAAAAAAAAAAAAA 
    
    while i in range(len(name)):
    
        
                # 상 하
        if name[i] != joystick[i]:
            if alphabet.count((name[i])) == 1:
                answer += alphabet.index((name[i])) #이미 A로 시작이므로 +1 하면 안됨
                joystick[i] = name[i]
            else:
                answer += alphabet2.index((name[i])) + 1
                joystick[i] = name[i]
        if name == ''.join(joystick): # 둘이 같으면 끝 (endpoint)
            break
        
        
               # 좌 우 , 비교, 도움, len(name)으로 나눈 나머지를 인덱스로한 값을 비교, 순환시킴
        left =1
        right =1
        #
        while name[(i +right) % len(name)] == joystick[(i +right) % len(name)]:
            right += 1
            
        while name[(i-left) % len(name)] == joystick[(i-left) % len(name)]:
            left += 1
       
        if right <=left: #오른쪽으로 가는게 왼쪽으로가는것보다 가까우면, 또는 왼쪽 오른쪽 둘다 A가 아니면
            answer += right #오른쪽 클릭만큼 더하고
            i = (i +right) % len(name) #커서위치 갱신
        else:
            answer += left # 왼쪽이 가까우면 왼쪽클릭만큼 더하고
            i = (i-left) % len(name) #커서위치 갱신
    return answer