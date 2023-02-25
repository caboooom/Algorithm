
n, m = map(int,input().split())


dp = [10001]*(m+1)

arr=[]
for i in range(n):
  arr.append(int(input()))

for i in arr:
  if i>m:
    arr.remove(i)

dp[0]=0
for i in range(len(arr)):
  for j in range(arr[i],m+1):
    if dp[j-arr[i]]!=10001:
      dp[j] = min(dp[j],dp[j-arr[i]]+1)

if dp[m]==10001:
  print(-1)
else:
  print(dp[m])
  
  