def solution(array):
    answer = []
    
    answer.append(max(array))
    for i in range(len(array)):
        if array[i] == answer[0]:
            answer.append(i)
    return answer