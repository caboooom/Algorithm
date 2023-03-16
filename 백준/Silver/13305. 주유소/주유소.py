import sys
input = sys.stdin.readline

n = int(input()) #도시의 개수
path_len = list(map(int,input().split())) #도로의 길이
oil_price = list(map(int,input().split()))

cost=0
curPrice=oil_price[0]
curPath=0
for i in range(1,n):
  #길이정보 갱신
  curPath += path_len[i-1]
  
  #기름값이 저렴해지면
  if curPrice > oil_price[i]:
    #지금까지의 비용합을 더해준다
    cost += curPath*curPrice

    #현재 기름값 정보를 갱신
    curPrice=oil_price[i]

    #길이정보도 초기화
    curPath = 0

  
if cost==0:
  cost = curPath*curPrice
print(cost)