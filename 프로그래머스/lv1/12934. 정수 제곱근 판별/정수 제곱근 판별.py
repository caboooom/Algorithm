def solution(n):

    factor = []
    i = 2
    while i <= n:
        if n % i == 0:
            factor.append(i)
            n /= i
        else:
            i += 1
    
    factor_set = set(factor)
    
    number = 1
    for i in factor_set:
        if factor.count(i) % 2 != 0:
            return -1
        number *= pow(i,factor.count(i)//2)
    return (number+1) ** 2