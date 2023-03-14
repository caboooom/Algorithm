import sys
input = sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
  arr.append(list(input().rstrip()))

#머리와 심장 찾기
head=[]
for i in range(n):
  if len(head)>0:
    break
  for j in range(n):
    if arr[i][j]=='*':
      head.append((i,j))
      break
heart = (head[0][0]+1,head[0][1])

#팔길이재기
leftArm=0
rightArm=0
for i in range(n):
  if arr[heart[0]][i]=='*':
    if i<heart[1]:
      leftArm += 1
    if i>heart[1]:
      rightArm += 1
    
#허리 재기
waist=0
for i in range(heart[0]+1,n):
  if arr[i][heart[1]]=='*':
    waist += 1
  else:
    break

#다리 재기
left,right=-1,-1
for i in range(n):
  if arr[heart[0]+1+waist][i]=='*':
      if left==-1:
        left=i
      else:
        right=i

leftLeg,rightLeg=0,0
for i in range(heart[0]+1+waist,n):
  if arr[i][left]=='*':
    leftLeg += 1
  if arr[i][right]=='*':
    rightLeg += 1

#결과 출력
print(heart[0]+1, heart[1]+1)
print(leftArm, rightArm, waist, leftLeg, rightLeg)