from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n,m = map(int,input().split())
    data = deque(map(int,input().split()))

    numbers = deque([i for i in range(n)])

    cnt = 0
    prior = 9
    while len(data) > 0:
      while True:
        if prior in data:
          break
        else:
          prior -= 1
      tempd, tempn = data.popleft(), numbers.popleft()
      if tempd == prior:
        cnt += 1
        if tempn == m:
          break
        
      else:
        data.append(tempd)
        numbers.append(tempn)
  
    print(cnt)