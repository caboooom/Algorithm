import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dict={}
for i in range(n):
  word = input().rstrip()
  if len(word)>=m:
    if word not in dict:
      dict[word]=[1,len(word)]
    else:
      dict[word][0] += 1

dict=sorted(dict.items(),key=lambda x:(-x[1][0],-x[1][1], x[0]))


for key,val in dict:
  print(key)