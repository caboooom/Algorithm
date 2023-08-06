import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(1001)]

max_h = 0
left = 1001
right = 0
for _ in range(n):
  l, h = map(int, input().split())
  arr[l] = h
  if h > max_h:
    max_h = h
    mid = l

for i in range(0,1001):
  if arr[i] > 0:
    left = i
    break
for i in range(1000,0,-1):
  if arr[i] > 0:
    right = i
    break



# max_h 가 여러 개인 경우, 오목하지 않도록 그 사이를 메꿔준다
if arr.count(max_h) > 1:
  temp_l = 0
  temp_r = 0
  for i in range(left, right+1):
    if arr[i] == max_h:
      temp_l = i
      break
  for i in range(right,0,-1):
    if arr[i] == max_h:
      temp_r = i
      break
  for i in range(temp_l, temp_r+1):
    arr[i] = max_h

# 왼쪽 메꿔준다
if arr[left] == max_h:
  pass
else:
  for i in range(left, mid):
    for j in range(i, mid):
      arr[j] = max(arr[i], arr[j])
  
# 오른쪽 메꿔준다
if arr[right] == max_h:
  pass
else:
  for i in range(right, mid, -1):
    for j in range(i, mid, -1):
      arr[j] = max(arr[i], arr[j])
  

print(sum(arr))