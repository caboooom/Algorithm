n, k = map(int,input().split())

arr = list(range(1,n+1))

result = []

idx = k-1
while len(arr) > 0:
  idx %= len(arr)
  result.append(arr.pop(idx))
  idx += (k-1)

answer = str(result)
answer = answer.replace('[', '<')
answer = answer.replace(']', '>')
print(answer)