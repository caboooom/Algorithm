import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

word = input().rstrip()
cond1 = set(word)
cond2 = Counter(word)

answer=0

for _ in range(n-1):
  new_word = input().rstrip()
  cond1_ = set(new_word)
  cond2_ = Counter(new_word)

  if abs(len(word)-len(new_word))>1:
    continue

  temp1 = cond2-cond2_
  temp2 = cond2_-cond2
  if len(temp1)>1 or len(temp2)>1:
    continue
  if len(temp1) == 1 and len(temp2) == 1:
    if temp1.most_common(1)[0][1] != temp2.most_common(1)[0][1]:
      continue
    if temp1.most_common(1)[0][1] != 1:
      continue
  
  answer += 1


print(answer)