import sys
input = sys.stdin.readline

n, m = map(int, input().split())

points = list(map(int,input().split()))
points.sort()

for _ in range(m):
  a, b = map(int, input().split())

  start = 0
  end = n-1
  while start <= end:
    mid = (start + end) // 2
    if points[mid] >= a:
      end = mid - 1
    else:
      start = mid + 1
  idx_a = end + 1
      
  start = 0
  end = n-1
  while start <= end:
    mid = (start + end) // 2
    if points[mid] > b:
      end = mid - 1
    else:
      start = mid + 1
  idx_b = end

  print(idx_b - idx_a + 1)