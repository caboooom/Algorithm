def solution(order):
    answer = 0
    arr=list(map(int,str(order)))
    for i in arr:
        if i in [3,6,9]:
            answer += 1
    return answer