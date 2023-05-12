from itertools import combinations_with_replacement

rnum = [50,10,5,1]

n = int(input())
result = set()
temp = list(combinations_with_replacement(rnum,n))
for i in temp:
  result.add(sum(i))

print(len(result))