import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))

block = [[0 for j in range(w)] for i in range(h)]
for i in range(w):
  for j in range(height[i]):
    block[j][i] = 1

answer = 0
for i in range(h):
  for j in range(w):
    if block[i][j] == 1:
      continue
    if 1 in block[i][:j] and 1 in block[i][j+1:]:
      answer += 1

print(answer)