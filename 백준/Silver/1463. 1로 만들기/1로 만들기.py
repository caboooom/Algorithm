x = int(input())

dp = [x]*(x+1)
dp[x]=0

for i in range(x):
  curNum = x-i

  if curNum%3==0:
    dp[curNum//3] = min(dp[curNum//3], dp[curNum]+1)
  if curNum%2==0:
    dp[curNum//2] = min(dp[curNum//2], dp[curNum]+1)
  dp[curNum-1] = min(dp[curNum-1], dp[curNum]+1)

print(dp[1])