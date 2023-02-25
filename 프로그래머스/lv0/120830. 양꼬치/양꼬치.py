def solution(n, k):
    if n//10 >=k:
        return 12000*n
    else:
        return 12000*n + 2000*(k-n//10)