def solution(n):
    dp = [0]*n
    dp[0] = 1 #1칸
    if n >= 2:
        dp[1] = 2 #1칸 또는 2칸
        for i in range(2,n):
            dp[i] = dp[i-2]%1234567 + dp[i-1]%1234567
    return dp[n-1]%1234567