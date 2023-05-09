import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))


  
idx = n
for i in range(n-1,0,-1):
  if data[i-1] < data[i]:
    idx = i-1
    break 
if idx == n:
  print(-1)
  exit()

for i in range(n-1,idx,-1):
  if data[i] > data[idx]:
    data[i], data[idx] = data[idx], data[i]
    break

answer = data[:idx+1] + sorted(data[idx+1:])
for i in range(n):
  print(answer[i],end=' ')