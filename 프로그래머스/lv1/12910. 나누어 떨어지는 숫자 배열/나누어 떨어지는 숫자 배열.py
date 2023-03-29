def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    answer.sort()
    return answer if len(answer)>0 else [-1]