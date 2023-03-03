import re
def solution(polynomial):
    poly = polynomial.split(" + ")

    a1,a2 = 0,0
    for i in poly:
        if str(i[-1])=="x":
            temp = i[:-1]
            a1+=1 if temp=="" else int(temp)
        else:
            a2 += int(i)
            
    answer=""
    if a1==1:
        answer += "x"
    if a1 > 1:
        answer += str(a1)+"x"
    if a2 >0:
        if a1==0:
            answer += str(a2)
        else:
            answer += " + "+str(a2)
    
    return answer