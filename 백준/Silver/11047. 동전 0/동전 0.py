import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for _ in range(n):
  temp = int(input())
  coins.append(temp)
coins.sort(reverse=True)

cnt = 0
idx = 0
while k > 0:
  if k // coins[idx] > 0 :
    cnt += (k//coins[idx])
    k %= coins[idx]
  else:
    idx += 1
print(cnt)