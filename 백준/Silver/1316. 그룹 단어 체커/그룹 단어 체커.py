import sys

def is_group_word(word):
  tempset = {word[0]}
  for i in range(0,len(word)-1):
    if word[i] != word[i+1]:
      if word[i+1] in tempset:
        return False
      else:
        tempset.add(word[i+1])
  return True

n = int(input())
answer = 0
for _ in range(n):
  word = sys.stdin.readline().rstrip()
  if is_group_word(word):
    answer += 1

print(answer)