def factorial(x):
    if x<=1:
        return 1
    return factorial(x-1)*x

def solution(n):
    result = 0
    i=0
    while factorial(i) <= n:
        result = max(result, factorial(i))
        i+=1
    return i-1