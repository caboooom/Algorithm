def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2,n+1):
        if isPrime(i)==False:
            answer+=1
    return answer