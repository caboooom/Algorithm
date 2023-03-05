def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append((abs(i-n),i))
    answer.sort(key = lambda x: (x[0], -x[1]))
    return [i[1] for i in answer]