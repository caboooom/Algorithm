h, w, n, m = map(int,input().split())

idx=0
row=0
while idx<h:
  idx += n+1
  row+=1

idx=0
col=0
while idx<w:
  idx += m+1
  col += 1

print(row*col)