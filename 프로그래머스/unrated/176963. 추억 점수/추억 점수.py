
def solution(name, yearning, photo):
    answer = []
    
    yearning_ = dict(zip(name,yearning))
    
    for p in photo:
        score = 0
        for i in range(len(p)):
            if p[i] in yearning_:
                score += yearning_[p[i]]
        answer.append(score)
        
    return answer