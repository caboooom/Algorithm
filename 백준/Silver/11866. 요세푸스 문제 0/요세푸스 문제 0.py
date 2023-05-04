
n, k = map(int,input().split())

answer = '<'

lst = [i for i in range(1,n+1)]

idx = 0
while len(lst) > 1:
  idx += k-1
  while idx > len(lst)-1:
    idx -= len(lst)
  answer += str(lst[idx]) + ', '
  del lst[idx]
answer += str(lst[0]) + '>'

print(answer)