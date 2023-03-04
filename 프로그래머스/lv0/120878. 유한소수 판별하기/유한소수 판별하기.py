def primeFactorization(n):
    result=[]
    i=2
    while i<=n:
        if n%i==0:
            result.append(i)
            n//=i
        else:
            i += 1
    return result

from fractions import Fraction
def solution(a, b):
    denom = Fraction(a,b).denominator
    
    for i in primeFactorization(denom):
        if i in [2,5]:
            continue
        else:
            return 2
    
    return 1