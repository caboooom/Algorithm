def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)):
        if len(lst) < k:
            lst.append(score[i])
        else:
            if min(lst) < score[i]:
                lst.remove(min(lst))
                lst.append(score[i])
        answer.append(min(lst))
    return answer