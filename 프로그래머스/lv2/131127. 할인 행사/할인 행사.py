from collections import deque
def solution(want, number, discount):
    answer = 0
    
    temp = deque(discount[:10])
    for i in range(10):
        if temp[i] in want:
            number[want.index(temp[i])] -= 1
    if set(want).issubset(set(temp)):
        if all(x<=0 for x in number):
            answer += 1
    
    n = len(discount)
    day = 0

    while day+10 < n:          
        # 맨앞 제품을 빼고 맨뒤에 제품추가    
        day += 1
        k = temp.popleft()
        if k in want:
            number[want.index(k)] += 1
            
        if day+9 < n:
            new = discount[day+9]
            temp.append(new)
            if new in want:
                number[want.index(new)] -= 1
            
        # 원하는 물건이 모두 들어있는지 체크
        if set(want).issubset(set(temp)):
            # 개수가 맞는지 체크
            if all(x<=0 for x in number):
                answer += 1
    return answer