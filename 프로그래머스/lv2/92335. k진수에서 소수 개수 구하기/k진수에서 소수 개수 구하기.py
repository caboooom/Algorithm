import math
def change(dec, k):
    result = []
    while dec // k > 0:
        result.append(str(dec % k))
        dec//= k
    result.append(str(dec))
    return ''.join(reversed(result))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    knum = change(n,k)
    
    klst = str(knum).split('0')
    for i in klst:
        if i == '':
            continue
        if isPrime(int(i)):
            answer += 1
    return answer