from collections import Counter

str = input()
str = str.upper()
cnt=Counter(str).most_common()

if len(cnt)==1:
  print(cnt[0][0])
else:
  if cnt[0][1]==cnt[1][1]:
    print("?")
  else:
    print(cnt[0][0])