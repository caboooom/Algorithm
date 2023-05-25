def solution(n, m, section):
    answer = 0       
            
    cur = 1
    idx = 0
    while idx < len(section):
        if cur <= section[idx]:
            cur = section[idx]
            answer += 1
            cur += m
        idx += 1
    return answer