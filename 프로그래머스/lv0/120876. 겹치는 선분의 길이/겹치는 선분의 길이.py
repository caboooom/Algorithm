def solution(lines):
    points = [0]*201
    
    for i in lines:
        x1, x2 = i[0]+100, i[1]+100
        for j in range(x1,x2):
            points[j] += 1

    answer = 0
    for i in points:
        if i >= 2:
            answer += 1

    return answer
 