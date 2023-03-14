import sys
input=sys.stdin.readline

n,k = map(int,input().split())
medals=[]
for i in range(n):
  medals.append(list(map(int,input().split())))

medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

medals[0][0]=1
rank=1
for i in range(1,len(medals)):
  if medals[i][1]==medals[i-1][1] and medals[i][2]==medals[i-1][2] and medals[i][3]==medals[i-1][3]:
    medals[i][0]=rank
  else:
    rank += 1
    medals[i][0]=rank

print(medals[k-1][0])