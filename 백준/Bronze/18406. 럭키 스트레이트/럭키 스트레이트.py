
a = input()
n = list(a)

left=0
right=0
for i in range(len(n)//2):
  left += int(n[i])
  right += int(n[-(i+1)])

if left==right:
  print("LUCKY")
else:
  print("READY")