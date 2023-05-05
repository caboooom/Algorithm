test = int(input())
for _ in range(test):
  data = input()
  stack = []
  flag = True
  for x in data:
    if x == "(":
      stack.append("(")
    else:
      if len(stack) > 0:
        stack.pop()
      else:
        flag = False
  if len(stack) > 0 :
    flag = False
  if flag:
    print("YES")
  else:
    print("NO")