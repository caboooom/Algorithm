import sys
input = sys.stdin.readline

arr=['a','e','i','o','u']

while True:
  test = input().rstrip()
  if test=="end":
    exit()

  acceptable=True
  vow=False
  
  if len(test)==1:
    if test in arr:
      vow=True
  if len(test)==2:
    if test[0] in arr or test[1] in arr:
      vow=True
    if test[0]==test[1]:
      if test[0]=="o" or test[0]=="e":
        pass
      else:
        acceptable=False
  if len(test)==3:
    if test[0] in arr or test[1] in arr or test[2] in arr:
      vow=True
    if test[1]==0 or test[1]==2:
      if test[1]=="o" or test[1]=="e":
        pass
      else:
        acceptable=False
    if test[0]==test[1]==test[2]:
      acceptable=False
    cnt1,cnt2=0,0
    for i in test:
      if i in arr:
        cnt1+=1
      else:
        cnt2+=1
    if cnt1==3 or cnt2==3:
      acceptable=False
  if len(test)>3:
    for i in range(len(test)):
      temp = test[i:i+3]
      cnt1 = 0 #모음의개수
      cnt2 = 0 #자음의개수
      for j in temp:
        if j in arr:
          cnt1 += 1
          vow=True
        else:
          cnt2 += 1
      #연속된 자음,모음 3글자 금지 조건
      if cnt1==3 or cnt2==3:
        acceptable=False
        break
      #연속된 두글자 금지 조건  
      if len(temp)>2:
        if temp[0]==temp[1] or temp[1]==temp[2]:
          if temp[1]=="e" or temp[1]=="o":
            pass
          else:
            acceptable=False
            break
        
  #모음 존재 조건
  if vow==False:
    acceptable=False

  #결과 출력
  if acceptable==True:
    print("<"+ test +"> is acceptable.")
  else:
    print('<'+test+'> is not acceptable.')