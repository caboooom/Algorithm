A=1
B=1
while True:
  A, B = map(int, input().split())
  if A==0 and B==0: break
  else: print("Yes" if A>B else "No")
