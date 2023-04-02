def solution(arr1, arr2):
    n = len(arr1)
    answer = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    
    return answer