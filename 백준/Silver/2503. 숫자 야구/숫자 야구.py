import sys
input = sys.stdin.readline

def check(num, a, b):
  first = num//100
  second = (num%100)//10
  third = num%10
  for i in range(123,988):
    if len(set([i//100, (i%100)//10, i%10])) != 3 or '0' in str(i):
      if i in ans_lst:
        ans_lst.remove(i)
      continue
    strike, ball = 0, 0
    if str(first) in str(i):
      ball += 1
    if str(second) in str(i):
      ball += 1
    if str(third) in str(i):
      ball += 1
    if first == i//100:
      ball -= 1
      strike += 1
    if second == (i%100)//10:
      ball -= 1
      strike += 1
    if third == i%10:
      ball -= 1
      strike += 1
    if strike == a and ball == b:
      pass
    else:
      if i in ans_lst:
        ans_lst.remove(i)

ans_lst = [i for i in range(123,988)]

n = int(input())
for _ in range(n):
  ans, strike, ball = map(int,input().split())
  if strike == 3:
    print(1)
    exit()
  check(ans,strike,ball)

print(len(ans_lst))
#print(ans_lst)