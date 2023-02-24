def solution(slice, n):
    ans=1
    while True:
        if slice*ans >= n:
            return ans
        ans += 1