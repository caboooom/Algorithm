import sys
input=sys.stdin.readline

s=input()

cnt=0
for i in range(1,len(s)):
  if s[i] != s[i-1]:
    cnt += 1

if s[0]!=s[-1]:
  cnt //= 2

print(cnt)