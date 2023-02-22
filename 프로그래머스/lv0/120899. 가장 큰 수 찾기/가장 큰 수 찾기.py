def solution(array):
    answer = []
    
#    return [max(array), array.index(max(array))]

    answer.append(max(array))
    for i in range(len(array)):
        if array[i] == answer[0]:
            answer.append(i)
            
    
    return answer

