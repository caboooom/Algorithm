from bisect import bisect_left, bisect_right

def sol(i):
  rightIdx = bisect_right(arr,i)
  leftIdx = bisect_left(arr,i)
  return rightIdx - leftIdx

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

m = int(input())
arr2 = map(int,input().split())

for i in arr2:
  print(sol(i),end=' ')
  