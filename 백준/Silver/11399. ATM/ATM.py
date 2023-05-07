import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data.sort()

waiting = 0
result = 0
for i in range(n):
  result += waiting + data[i]
  waiting += data[i]

print(result)