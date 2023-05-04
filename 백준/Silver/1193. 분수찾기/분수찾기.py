x = int(input())
 
flag = True
n = 1
nCnt = 1
den, num = 0, 0 # 분모, 분자
while flag:
  for i in range(1,n+1):
    nCnt += 1
    if nCnt > x:
      if n%2 == 0:
        den = i
        num = n-i+1
      else:
        den = n-i+1
        num = i
      flag = False
      break
  n += 1
  

print('{}/{}'.format(den,num))