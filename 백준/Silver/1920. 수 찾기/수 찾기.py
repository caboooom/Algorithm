import sys
input = sys.stdin.readline

def isExist(x,arr):
  start=0
  end=n-1

  if x>arr[end] or x<arr[start]:
    return 0

      
  while start<=end:
    mid = (start+end)//2
    if arr[mid]==x:
      return 1
    elif arr[mid]>x:
      end=mid-1
    else:
      start=mid+1
  return 0


n = int(input())
arr=list(map(int,input().split()))
arr.sort()

m = int(input())
arr2=list(map(int,input().split()))

for i in range(m):
  print(isExist(arr2[i],arr));