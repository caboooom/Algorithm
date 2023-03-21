import sys 
input = sys.stdin.readline

n = int(input())
time = [0]*n
price = [0]*n

for i in range(n):
  t, p = map(int,input().split())
  time[i] = t
  price[i] = p

dp = [0]*(n+1)
for i in range(n):
  j = i + time[i]
  while j <= n:
    dp[j] = max(dp[j], price[i]+dp[i])
    j += 1

print(dp[n])