from itertools import combinations

def solution(number):
    answer = 0
    for combi in list(combinations(number,3)):
        a, b, c = combi
        if a + b + c == 0:
            answer += 1
    return answer