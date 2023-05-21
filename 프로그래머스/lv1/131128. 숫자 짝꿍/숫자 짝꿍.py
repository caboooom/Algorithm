def solution(X, Y):
    answer = []
    
    numx = [0]*10
    numy = [0]*10
    for i in X:
        numx[int(i)] += 1
    for i in Y:
        numy[int(i)] += 1
    
    for i in range(9,-1,-1):
        if numx[i]>0 and numy[i]>0:
            j = min(numx[i],numy[i])
            for _ in range(j):
                answer.append(str(i))
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return ''.join(answer)