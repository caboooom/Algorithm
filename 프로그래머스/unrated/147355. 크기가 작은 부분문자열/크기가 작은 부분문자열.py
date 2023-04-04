def solution(t, p):
    answer = 0
    l = len(p)
    i = 0
    while i+l <= len(t):
        temp = t[i:i+l]
        if temp <= p:
            answer += 1
        i += 1
    return answer