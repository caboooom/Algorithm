def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

def LCM(a,b):
    return a * b // GCD(a,b)

def solution(n, m):
    if n < m:
        n, m = m, n
    return [GCD(n,m), LCM(n,m)]