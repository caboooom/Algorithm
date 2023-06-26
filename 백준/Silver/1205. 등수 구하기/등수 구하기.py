
n, taesu, p = map(int, input().split())

if n > 0:
  scores = list(map(int,input().split()))
else:
  scores = []
scores.append(taesu)

rank_list = [0 for i in range(p)]

scores.sort(reverse=True)
for i in range(p):
  if i >= len(scores):
    break
  rank_list[i] = scores[i]


if taesu not in rank_list:
  print(-1)
  exit(0)

## 태수와 동점인 점수가 원래 리스트에 k개 있었고
## 그 점수가 랭킹리스트에 k개 존재하지 않는다면 태수는 랭크가 없는것

k = scores.count(taesu)
if rank_list.count(taesu) < k:
  print(-1)
  exit(0)

rank = 0
same = 1
prev = -1
for score in rank_list:
  if score == taesu:
    rank += same
    break
  if prev == score:
    same += 1
  else:
    rank += same
    same = 1
  prev = score

print(rank)