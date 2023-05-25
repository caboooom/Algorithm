def solution(n, m, section):
    section = set(section)
    answer = 0       
    idx = 1
    while idx <= n:
        if idx in section:
            answer += 1
            idx += m
        else:
            idx += 1
    return answer