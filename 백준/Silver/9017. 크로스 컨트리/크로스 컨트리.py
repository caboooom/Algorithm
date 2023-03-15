import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))

  #6명 모두 완주한 팀 구하기
  temp=[0]*201
  qualified=[]
  for i in range(n):
    temp[arr[i]] += 1
    if temp[arr[i]]==6:
      qualified.append(arr[i])

  #실격팀제외, 배열만들기
  mainArr=[]
  for i in range(n):
    if arr[i] in qualified:
      mainArr.append(arr[i])

  #최종 점수 매기기
  final_score = []
  for i in range(len(qualified)):
    tempList=[qualified[i],0,0,0] #팀번호,점수,들어온사람,5번
    final_score.append(tempList)
  
  for i in range(len(mainArr)):
    for j in range(len(final_score)):
      if final_score[j][0]==mainArr[i]:
        if final_score[j][2]<4:
          final_score[j][2]+=1
          final_score[j][1]+=(i+1)
        elif final_score[j][2]==4:
          if final_score[j][3]==0:
            final_score[j][3] += (i+1)
        

  final_score.sort(key=lambda x:(x[1],x[3]))

  print(final_score[0][0])
        
