import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))

result=[-1]*n

for i in range(n):
  cnt=0
  for j in range(n):
    if result[j]==-1:
      if cnt>=arr[i]:
        result[j]=i+1
        break
      else:
        cnt+=1
 
for i in range(n):
  print(result[i],end=' ')