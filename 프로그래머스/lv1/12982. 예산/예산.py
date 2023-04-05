def solution(d, budget):
    answer = 0
    d.sort()
    current = 0
    for i in range(len(d)):
        current += d[i]
        if current > budget:
            break
        answer += 1
    return answer