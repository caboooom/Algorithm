import sys
input = sys.stdin.readline

str = list(input().rstrip())

a_num = str.count('a')
ans=1001

left=0
while left < len(str):
  right = left + a_num
  if right > len(str):
    temp = str[left:len(str)] + str[:right-len(str)]
  else:
    temp = str[left:right]
  ans = min(ans,temp.count('b'))
  left += 1

print(ans)