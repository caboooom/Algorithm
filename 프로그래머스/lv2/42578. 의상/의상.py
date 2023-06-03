from functools import reduce

def solution(clothes):
    cdict = dict()
    for cname, ctype in clothes:
        if ctype not in cdict:
            cdict[ctype] = 1
        else:
            cdict[ctype] += 1
            
    answer = 1
    for x in cdict:
        answer *= (cdict[x]+1)
    
    return answer-1