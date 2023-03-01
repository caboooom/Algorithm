from itertools import combinations

def dist(x,y,chicken):
  minDist=101
  for i in range(len(chicken)):
    a = chicken[i][0]
    b = chicken[i][1]
    minDist = min(minDist, abs(x-a)+abs(y-b))
  return minDist

n, m = map(int,input().split())

graph =[]
for i in range(n):
  graph.append(list(map(int,input().split())))


#치킨집과 집 좌표 모두 저장
chickens=[]
home=[]
for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      home.append((i,j))
    if graph[i][j]==2:
      chickens.append((i,j))

#폐점할 필요가 없다면 치킨거리를 출력
curDist=0
if len(chickens) <= m:
  for h in range(len(home)):
    curX = home[h][0]
    curY = home[h][1]
    curDist += dist(curX,curY,chickens)
  print(curDist)
  exit()

#폐점해야할경우 가능한 모든 경우 검사해본다
minDist=int(1e9)
comb= list(combinations(chickens,m))

for l in range (len(comb)):
  curDist=0
  for h in range(len(home)):
    curX = home[h][0]
    curY = home[h][1]
    curDist += dist(curX,curY,comb[l])
  minDist = min(minDist,curDist)

print(minDist)
