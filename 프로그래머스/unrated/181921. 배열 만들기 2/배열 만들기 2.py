def solution(l, r):
    answer = []
    for i in range(l,r+1):
        temp = str(i)
        temp = temp.replace("0","")
        temp = temp.replace("5","")
        if temp == "":
            answer.append(i)
    return answer if len(answer)>0 else [-1]