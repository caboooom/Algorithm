import sys 
input = sys.stdin.readline
from collections import Counter

def find_mode(data):
  cnt = Counter(data)
  cnt = cnt.most_common()
  if cnt[0][1] == cnt[1][1]:
    return cnt[1][0]
  else:
    return cnt[0][0]
  
data = []

n = int(input())
for _ in range(n):
  x = int(input())
  data.append(x)

if n == 1:
  print(x)
  print(x)
  print(x)
  print(0)
  exit()

data.sort()

print(int(round(sum(data)/n,0)))
print(data[n//2])
print(find_mode(data))
print(data[-1]-data[0])