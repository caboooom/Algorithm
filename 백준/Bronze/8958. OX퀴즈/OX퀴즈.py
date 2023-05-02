import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
  testcase = input().rstrip()
  score = 0
  total = 0
  for problem in testcase:
    if problem == "O":
      score += 1
      total += score
    else:
      score = 0
  print(total)
  
  