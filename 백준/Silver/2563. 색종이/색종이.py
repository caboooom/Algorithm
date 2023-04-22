import sys
input = sys.stdin.readline

n = int(input())

background = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
  a, b = map(int,input().split())
  for i in range(b,b+10):
    for j in range(a,a+10):
      background[i][j] = 1
      
answer = 0
for i in range(100):
  answer += background[i].count(1)

print(answer)
