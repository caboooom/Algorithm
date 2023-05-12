move = {"LT":[-1,-1],"T":[-1,0], "RT":[-1,1], "R":[0,1],
        "RB":[1,1], "B":[1,0], "LB":[1,-1], "L":[0,-1]}

cols = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

king, rock, n = input().split()

kx = 8 - int(king[1])
ky = cols[king[0]]
rx = 8 - int(rock[1])
ry = cols[rock[0]]


for _ in range(int(n)):
  command = input()
  nkx, nky = move[command]
  nkx += kx
  nky += ky
  flag = True
  if 0 <= nkx < 8 and 0 <= nky < 8:
    if nkx == rx and nky == ry:
      nrx, nry = move[command]
      nrx += rx
      nry += ry
      if 0 <= nrx < 8 and 0 <= nry < 8:
        rx, ry = nrx, nry
      else:
        flag = False
    if flag:
      kx, ky = nkx, nky

king = ''
rock = ''
for i in cols:
  if cols[i] == ky:
    king += i
  if cols[i] == ry:
    rock += i
king += str(8-kx)
rock += str(8-rx)

print(king)
print(rock)