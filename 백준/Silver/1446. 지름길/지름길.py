import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

n, d = map(int, input().split())
dp = [INF for i in range(10001)]
shortcut = []
for _ in range(n):
  shortcut.append ( list(map(int, input().split())) )

shortcut.sort()
shortcut = deque(shortcut)

cur = 0
end = 0
slen = 0
dp[0] = 0

for i in range(d+1):
  dp[i] = min(dp[i-1]+1, dp[i])
  if len(shortcut)>0 and shortcut[0][0] <= i:
    cur, end, slen = shortcut.popleft()
    dp[end] = min(dp[end], dp[cur] + slen)
    cur = 0
print(dp[d])
