from collections import Counter

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
cnt = Counter(result)

result = [0 for i in range(10)]

for i in cnt:
  result[int(i)] = cnt[i]

for i in range(10):
  print(result[i])
  