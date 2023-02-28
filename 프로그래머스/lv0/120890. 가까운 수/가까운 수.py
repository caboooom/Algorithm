
def solution(array, n):
    arr=[abs(i-n) for i in array]
    temp = []
    for i in range(len(arr)):
        if arr[i]==min(arr):
            temp.append(array[i])
    return min(temp)