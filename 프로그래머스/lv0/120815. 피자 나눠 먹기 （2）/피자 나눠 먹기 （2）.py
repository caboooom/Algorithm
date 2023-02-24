def solution(n):
    ans=1
    while True:
        if 6 * ans % n ==0:
            return ans
        ans += 1