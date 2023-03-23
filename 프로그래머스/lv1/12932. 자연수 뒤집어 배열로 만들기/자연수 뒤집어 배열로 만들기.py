def solution(n):
    answer = []
    digits = list(''.join(str(n)))
    digits.reverse()
    for i in range(len(digits)):
        answer.append(int(digits[i]))
    return answer