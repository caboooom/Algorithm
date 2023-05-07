import sys
input = sys.stdin.readline

n, m = map(int,input().split())
notseen = set()
notheard = set()
for _ in range(n):
  temp = input().rstrip()
  notseen.add(temp)
for _ in range(m):
  temp = input().rstrip()
  notheard.add(temp)

answer = list(notseen & notheard)
answer.sort()
print(len(answer))
for i in range(len(answer)):
  print(answer[i])