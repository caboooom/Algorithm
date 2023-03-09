def solution(N, stages):
    answer = []
    
    arr1=[0]*200001
    arr2=[0]*200001
    
    for i in stages:
        arr1[i] += 1
        for j in range(1,i+1):
            arr2[j] += 1
            
    arr=[]
    for i in range(1,200001):
        if arr2[i] != 0:
            arr.append((arr1[i]/arr2[i],i))
        if arr2[i] == 0 and i<=N:
            arr.append((0,i))
            
    arr.sort(key=lambda x:(-x[0],x[1]))
    for rate,num in arr:
        if num<=N:
            answer.append(num)
    return answer