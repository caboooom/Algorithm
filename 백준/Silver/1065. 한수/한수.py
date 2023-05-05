n = int(input())

answer = 0
for i in range(1,n+1):
  if i < 100:
    answer += 1
    continue 
  cur = str(i)
  diff = int(cur[1])-int(cur[0])
  flag = True
  for x in range(1,len(cur)):
    if int(cur[x]) - int(cur[x-1]) != diff:
      flag = False
      break
  if flag:
    answer += 1

print(answer)