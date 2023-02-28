import sys
input = sys.stdin.readline

def budget(x):
  result=0
  for i in range(n):
    if x>=requests[i]:
      result += requests[i]
    else:
      result += x
  return result

n = int(input())
requests=list(map(int,input().split()))
m = int(input())

requests.sort()

if requests[-1]*n <= m:
  print(requests[-1])
  exit()

start=0
end=requests[-1]

result=0

while start<=end:
  mid = (start+end)//2
  temp=budget(mid)
  if temp<=m:
    result=mid
    start=mid+1
  else:
    end=mid-1

print(result)
