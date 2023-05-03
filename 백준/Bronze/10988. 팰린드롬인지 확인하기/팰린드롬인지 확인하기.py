import sys
input = sys.stdin.readline

word = input().rstrip()
temp = list(word)
rword = ''.join(reversed(temp))
if word == rword:
  print(1)
else:
  print(0)