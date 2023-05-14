def solution(food):
    front, end = [], []
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            front.append(str(i))
            end.append(str(i))
    end.reverse()
    result = front + ['0'] + end # 물은 항상 1개
    
    return ''.join(result)