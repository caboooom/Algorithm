def to_binary(x,n):
    result=[]
    while x>1:
        result.append(x%2)
        x //= 2
    result.append(x)
    while True:
        if len(result)==n:
            break
        else:
            result.append(0)
    result.reverse()
    return result

def solution(n, arr1, arr2):
    answer = [[] * n for _ in range(n)]
    
    for i in range(n):
        temp=""
        b1 = to_binary(arr1[i],n)
        b2 = to_binary(arr2[i],n)
        for j in range(n):
            if b1[j]==1 or b2[j]==1:
                temp += "#"
            else:
                temp += " "
        answer[i]=temp
    return answer