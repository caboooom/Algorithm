def solution(n):
    answer = 0
    for i in range(1,n+1):
        temp = i
        if temp == n:
            answer += 1
            break
        for j in range(i+1,n+1):
            temp += j
            if temp == n:
                answer += 1
            elif temp > n:
                break
    return answer