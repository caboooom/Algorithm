def solution(n):
    number = list(str(n))
    number.sort(reverse = True)
    answer = int(''.join(number))
    return answer