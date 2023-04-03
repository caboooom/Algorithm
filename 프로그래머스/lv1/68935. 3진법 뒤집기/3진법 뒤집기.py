def solution(n):
    answer = 0
    
    # 10진수를 3진수로 변환
    result = []
    while n >= 1:
        result.append(n%3)
        n //= 3
    result.reverse()
    
    # 앞뒤 반전 3진수를 10진수로 변환
    for i in range(len(result)):
        answer += pow(3,i) * result[i]

    
    return answer