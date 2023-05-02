import sys
input = sys.stdin.readline

while True:
  n = input().rstrip()
  if n == "0":
    break

  reversed_n = ''
  for i in range(1,len(n)+1):
    reversed_n += n[-i]
  if n == reversed_n:
    print("yes")
  else:
    print("no")