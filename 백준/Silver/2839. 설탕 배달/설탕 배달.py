n = int(input())

answer = 0
if n//5 > 0:
  answer += n//5
  n %= 5

while n%3 != 0 and answer > 0:
  answer -= 1
  n += 5

if n//3 > 0:
  answer += n//3
  n %= 3

if n > 0:
  print(-1)
else:
  print(answer)