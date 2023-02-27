def solution(numbers, k):
    arr=[]
    for i in range(0,len(numbers),2):
        arr.append(numbers[i])
    if len(numbers)%2!=0:
        for i in range(1,len(numbers),2):
            arr.append(numbers[i])
        
    return arr[k%len(arr)-1]