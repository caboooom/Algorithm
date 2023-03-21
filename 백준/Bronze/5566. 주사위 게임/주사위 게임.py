import sys 
input = sys.stdin.readline

n, m = map(int,input().split())

map=[0]*2000
for i in range(n):
  x = int(input())
  map[i]=x

dice = []
for i in range(m):
  dice.append(int(input()))

pos, cnt = 0, 0
for i in range(m):
  pos += dice[i]
  pos += map[pos]
  cnt += 1
  if pos >= n-1:
    break
print(cnt)
  