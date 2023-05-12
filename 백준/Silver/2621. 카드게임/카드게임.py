color = []
number = []
ncnt = [0,0,0,0,0,0,0,0,0]

for _ in range(5):
  c, n = input().split()
  color.append(c)
  number.append(int(n))
  ncnt[int(n)-1] += 1
number.sort()
score = 0

# 1
flag = True
for i in range(4):
  if number[i] + 1 != number[i+1]:
    flag = False
    break
if flag and len(set(color)) == 1:
  score = max(number) + 900

# 2
if 4 in ncnt:
  idx = 0
  for i in range(9):
    if ncnt[i] == 4:
      idx = i + 1
      break
  score = max(score, idx + 800)
# 3
two, three = 0, 0
for i in range(9):
  if ncnt[i] == 2:
    two = i + 1
  if ncnt[i] == 3:
    three = i + 1
if two > 0 and three > 0:
  score = max(score, three*10 + two + 700)

# 4
if len(set(color)) == 1:
  score = max(score, max(number) + 600)

# 5
if flag:
  score = max(score, max(number) + 500)

# 6
if three > 0:
  score = max(score, three + 400)

# 8
if two > 0:
  score = max(score, two + 200)

# 7
t1, t2 = 0, 0
for i in range(9):
  if ncnt[i] == 2:
    if t1 == 0:
      t1 = i + 1
    else:
      t2 = i + 1
if t1 > 0 and t2 > 0:
  score = max(score, t2 * 10 + t1 + 300)

# 9
if score == 0:
  score = max(number) + 100

print(score)
    