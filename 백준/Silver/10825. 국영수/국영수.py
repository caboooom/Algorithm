data=[]
n = int(input())
for i in range(n):
  name, ks, es, ms = input().split()
  data.append((name,ks,es,ms))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
  print(data[i][0])