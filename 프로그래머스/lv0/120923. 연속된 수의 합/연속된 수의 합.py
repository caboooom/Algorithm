def solution(num, total):
    answer = []
    start=-total
    end=total
    if total==0:
        start,end = -num,num
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in range(num):
            sum += mid+i
        if sum>total:
            end = mid-1
        elif sum<total:
            start = mid+1
        else:
            break
    for i in range(num):
        answer.append(mid+i)
    return answer