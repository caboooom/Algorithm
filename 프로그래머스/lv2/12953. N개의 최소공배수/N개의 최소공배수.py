def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)
    
def LCM(a,b):
    return a*b // GCD(a,b)

def solution(arr):
    answer = 0
    if len(arr) == 1:
        return arr[0]
    answer = LCM(arr[0],arr[1])
    
    for i in range(2,len(arr)):
        answer = LCM(answer, arr[i])
    return answer