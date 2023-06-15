from itertools import permutations

def calc(k, ordered_lst):
    result = 0
    for a, b in ordered_lst:
        if a > k or b > k:
            return result
        k -= b
        result += 1
    return result

def solution(k, dungeons):
    answer = 0
    for order in list(permutations(dungeons)):
        answer = max(answer, calc(k, order))
    return answer