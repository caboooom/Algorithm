import sys
input = sys.stdin.readline

str = list(input().rstrip())

a_num = str.count('a')
ans=1001

start=0
while start < len(str):
  end = start + a_num
  if end > len(str):
    temp = str[start:len(str)] + str[:end-len(str)]
  else:
    temp = str[start:end]
  ans = min(ans,temp.count('b'))
  start += 1

print(ans)