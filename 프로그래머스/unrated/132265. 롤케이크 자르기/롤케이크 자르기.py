from collections import Counter

def solution(topping):
    answer = 0
    lcounter = Counter(topping)
    rset = set()
    l = len(set(lcounter))
    r = 0
    
    for i in range(len(topping)):
        lcounter[topping[-1]] -= 1
        if lcounter[topping[-1]] == 0:
            l -= 1
        if topping[-1] not in rset:
            r += 1
            rset.add(topping[-1])   
        topping.pop()
        
        if l == r:
            answer += 1
            
    return answer