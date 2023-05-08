import sys
input = sys.stdin.readline

def reverse_str(input_str):
  temp = list(input_str)
  temp.reverse()
  return ''.join(temp)

s = input().rstrip()
result = ''
idx = 0
while idx < len(s):
  start = idx
  if s[idx] == '<':
    while s[idx] != '>':
      idx += 1
    idx += 1
    result += s[start:idx]
  else:
    while True:
      idx += 1
      if idx == len(s) or s[idx] == '<' or s[idx] == ' ':
        break
    result += reverse_str(s[start:idx]).rstrip(' ')
    if idx < len(s) and s[idx] == ' ':
      result += ' '
print(result)