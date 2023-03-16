import sys
input = sys.stdin.readline

n,k = map(int,input().split())
table = list(input().rstrip())

cnt = 0
for i in range(n):
  if table[i]=='P':
    j=k
    while j >= -k:
      if 0 <= i-j < n and table[i-j]=='H':
        table[i-j]='X'
        cnt += 1
        break
      j -= 1
print(cnt)