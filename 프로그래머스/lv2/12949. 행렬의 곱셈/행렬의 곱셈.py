def solution(arr1, arr2):
    row, col = len(arr1), len(arr2[0])
    answer = [[0 for j in range(col)] for i in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer