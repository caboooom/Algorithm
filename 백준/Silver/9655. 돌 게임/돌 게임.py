
n = int(input())

winner="CY"
while n>0:
  if n>=3:
    n -= 3
  else:
    n -= 1
  if winner=="SK":
    winner = "CY"
  else:
    winner="SK"
print(winner)