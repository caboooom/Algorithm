import sys
input=sys.stdin.readline

p = int(input())
for case in range(p):
  arr = list(map(int,input().split()))
  sortedArr=[arr[1]]
  cnt = 0
  for i in range(2,21):
    sortedArr.append(arr[i])
    j=i-1
    while j>0:
      if sortedArr[j] < sortedArr[j-1]:
        sortedArr[j-1],sortedArr[j] = sortedArr[j],sortedArr[j-1]
        cnt += 1
      j -= 1
  print(arr[0], cnt)