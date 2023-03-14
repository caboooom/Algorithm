import sys
input=sys.stdin.readline

m=int(input())
mySet=set()
for i in range(m):
  operation = input().rstrip()
  if operation=="all":
    mySet.clear()
    mySet.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

  elif operation=="empty":
    mySet.clear()

  else:
    operation, x = operation.split()
  
  if operation=="add":
    mySet.add(int(x))
  if operation=="remove":
    mySet.discard(int(x))
  if operation=="check":
    if int(x) in mySet:
      print("1")
    else:
      print("0")
  if operation=="toggle":
    if int(x) in mySet:
      mySet.remove(int(x))
    else:
      mySet.add(int(x))