def solution(N, stages):
    answer = []
    
    failed=[0]*502
    cleared=[0]*502
    
    for i in stages:
        failed[i] += 1
        for j in range(1,i+1):
            cleared[j] += 1
            
    arr=[]
    for i in range(1,N+1):
        if cleared[i] != 0:
            arr.append((failed[i]/cleared[i],i))
        else:
            arr.append((0,i))
    
    arr.sort(key=lambda x:(-x[0],x[1]))
    
    for rate,num in arr:
        if num<=N:
            answer.append(num)
    return answer
