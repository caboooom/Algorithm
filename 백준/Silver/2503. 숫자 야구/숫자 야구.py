import sys
input = sys.stdin.readline

def check(q, a, b):
  qnum = [q//100, (q%100)//10, q%10] # 영수가 말한 답
  for i in range(123,988):
    if i not in ans_lst:
      continue
    strike, ball = 0, 0
    inum = [i//100, (i%100)//10, i%10]
    for j in range(3):
      if qnum[j] in inum:
        ball += 1
      if qnum[j] == inum[j]:
        strike += 1
        ball -= 1
    if strike == a and ball == b:
      pass
    else:
      if i in ans_lst:
        ans_lst.remove(i)

# 정답 후보 리스트
ans_lst = [i for i in range(123,988)]
for i in range(123,988):
  if len(set([i//100, (i%100)//10, i%10])) != 3 or '0' in str(i):
      if i in ans_lst:
        ans_lst.remove(i)
        
n = int(input())
for _ in range(n):
  x, y, z = map(int,input().split())
  if y == 3:
    print(1)
    exit()
  check(x,y,z)

print(len(ans_lst))