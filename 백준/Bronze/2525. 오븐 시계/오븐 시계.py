
A, B = map(int, input().split())
C = int(input()) + B
B = 0

if C >= 60:
  hour = C//60
  min = C%60
else:
  hour=0
  min=C

if A + hour >= 24:
  A = A + hour - 24
else:
  A += hour
B += min

print(A, B)