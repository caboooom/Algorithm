import sys
input = sys.stdin.readline

n = input().rstrip()


setnum = 0

for i in range(10):
  if i == 6 or i == 9:
    continue
  setnum = max(setnum, n.count(str(i)))

six = n.count("6")
nine = n.count("9")


if six + nine <= 2 * setnum:
  print(setnum)
else:
  if (six + nine) % 2 == 0:
    print((six+nine)//2)
  else:
    print((six+nine)//2+1)
