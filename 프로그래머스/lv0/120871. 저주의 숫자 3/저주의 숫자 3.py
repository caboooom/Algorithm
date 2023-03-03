def solution(n):
    num = 0
    for i in range(1,n+1):
        num += 1
        while num%3==0 or '3' in str(num):
            num += 1
    return num