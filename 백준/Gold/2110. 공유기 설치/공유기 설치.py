import sys
input = sys.stdin.readline

n, c = map(int,input().split())
houses=[]
for i in range(n):
  houses.append(int(input()))

houses.sort()

start = 0
end = houses[-1]-houses[0]
answer = 0

while start <= end:
  mid = (start+end)//2
  cur = houses[0]
  cnt=1

  for i in range(1,n):
    if houses[i] >= cur+mid:
      cur=houses[i]
      cnt += 1
  if cnt >= c:
    start = mid+1
    answer=mid
  else:
    end = mid-1

print(answer)