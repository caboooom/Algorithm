def calc_score(score,bonus,option):
    result=[0,0,0]
    for i in range(3):
        if bonus[i] == "S":
            result[i] += score[i]
        elif bonus[i] == "D":
            result[i] += score[i]**2
        else:
            result[i] += pow(score[i],3)
        
        if option[i] == "*":
            result[i] *= 2
            if i>0:
                result[i-1] *= 2
        if option[i] == "#":
            result[i] *= (-1)
    return result

def solution(dartResult):
    score=[]
    bonus=[]
    option=[]
    
    i=0
    while i<len(dartResult):
        if dartResult[i:i+2].isdigit():
            score.append(int(dartResult[i:i+2]))
            i += 2
        else:
            score.append(int(dartResult[i]))
            i += 1
        bonus.append(dartResult[i])
        i += 1
        if i>= len(dartResult):
            option.append("N")
            break
        if dartResult[i].isdigit():
            option.append("N")
        else:
            option.append(dartResult[i])
            i += 1
            
    answer = sum(calc_score(score,bonus,option))
    return answer