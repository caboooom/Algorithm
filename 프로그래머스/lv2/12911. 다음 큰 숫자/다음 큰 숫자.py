def solution(n):
    cnt = bin(n)[2:].count("1")

    next = n+1
    while True:
        if bin(next)[2:].count("1") == cnt:
            return next
        next += 1