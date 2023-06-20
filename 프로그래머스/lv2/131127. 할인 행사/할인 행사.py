from collections import deque
def solution(want, number, discount):
    answer = 0
    
    temp = deque(discount[:10])
    for i in range(10):
        if temp[i] in want:
            number[want.index(temp[i])] -= 1
    
    if set(want).issubset(set(temp)):
            flag = True
            for j in range(len(number)):
                if number[j] > 0:
                    flag = False
                    break
            if flag:
                answer += 1
            
    n = len(discount)
    day = 0

    while day+10 < n:          
        # 맨앞 제품을 빼고 맨뒤에 제품추가    
        day += 1
        k = temp.popleft()
        try:
            idx = want.index(k)
            number[idx] += 1
        except:
            pass
            
        if day+9 < n:
            temp.append(discount[day+9]) 
            try:
                idx = want.index(discount[day+9])
                number[idx] -= 1
            except:
                pass
            
        # 원하는 물건이 모두 들어있는지 체크
        if set(want).issubset(set(temp)):
            # 개수가 맞는지 체크
            flag = True
            for j in range(len(number)):
                if number[j] > 0:
                    flag = False
                    break
            if flag:
                answer += 1
    
    return answer