import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  k = int(input())
  n = int(input())

  dp=[[i for i in range(n+1)]]

  #k층 n호
  for i in range(1,k+1):
    dp.append([0]*(n+1))
    for j in range(1,n+1):
      dp[i][j]=dp[i][j-1]+dp[i-1][j]

  print(dp[k][n])