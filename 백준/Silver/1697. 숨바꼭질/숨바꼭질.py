from collections import deque

n, k = map(int, input().split())

answer = 0
q = deque()
q.append(n)

arr = [0 for _ in range(100001)]
arr[n] = 1
while q:
  cur = q.popleft()
  if cur == k:
    print(arr[cur]-1)
    break
  for next in [cur*2, cur+1, cur-1]:
    if 0 <= next < 100001 and arr[next] == 0:
      arr[next] = arr[cur] + 1
      q.append(next)