def solution(score):
    avg=[sum(i)/2 for i in score]
    avg.sort(reverse=True)
    
    answer=[]
    for i in range(len(score)):
        answer.append(avg.index(sum(score[i])/2)+1)
    return answer