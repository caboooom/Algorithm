A, B, C = map(int, input().split())
D = int(input())

#초설정
if C+D >= 60:
  B += (C+D)//60
  C = (C+D)%60
else:
  C += D

#분설정
if B >= 60:
  A += B//60
  B %= 60

#시설정
if A >= 24:
  while A>=24: A -= 24

print(A,B,C)