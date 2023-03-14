n = int(input())
arr=[]
for i in range(n):
  arr.append(list(map(int,input().split())))

#자신보다 덩치가 큰 사람 수 세기
for i in range(n):
  cnt=0
  for j in range(n):
    if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
      cnt += 1
  arr[i].append(cnt)

#출력
for i in range(n):
  print(arr[i][2]+1,end=' ')