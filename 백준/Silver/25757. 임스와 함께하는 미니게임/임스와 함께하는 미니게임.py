import sys
input=sys.stdin.readline

n, game = input().split()
name=set()
for i in range(int(n)):
  name.add(input().rstrip())

if game=='Y':
  print(len(name))
if game=='F':
  print(len(name)//2)
if game=='O':
  print(len(name)//3)