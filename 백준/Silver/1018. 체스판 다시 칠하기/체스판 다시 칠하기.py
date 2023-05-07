import sys
input = sys.stdin.readline


def repaint(a,b):
  odd = "WBWBWBWB"
  even = "BWBWBWBW"
  result1 = 0
  result2 = 0
  for i in range(a,a+8):
    for j in range(b,b+8):
      idx = j-b
      if i%2 != 0:
        if odd[idx] != board[i][j]:
          result1 += 1
        if even[idx] != board[i][j]:
          result2 += 1
      else:
        if even[idx] != board[i][j]:
          result1 += 1
        if odd[idx] != board[i][j]:
          result2 += 1
  return min(result1,result2)

n, m = map(int,input().split())
board = []
for _ in range(n):
  temp = list(input())
  board.append(temp)

answer = int(1e9)
a,b = 0,0
for i in range(n):
  for j in range(m):
    if a+8 <= n and b+8 <= m:
      answer = min(answer,repaint(a,b))
    b += 1
  a += 1
  b = 0

print(answer)