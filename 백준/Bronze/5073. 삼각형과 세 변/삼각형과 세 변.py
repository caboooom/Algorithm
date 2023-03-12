
while True:
  a,b,c = map(int,input().split())
  if a==0 and b==0 and c==0:
    exit()

  arr = [a,b,c]
  arr.sort()
  
  if a==b and b==c:
    print("Equilateral")
  elif arr[2] >= arr[0]+arr[1]:
    print("Invalid")
  elif arr[0]==arr[1] and arr[1]!=arr[2]:
    print("Isosceles")
  elif arr[0]!=arr[1] and arr[1]==arr[2]:
    print("Isosceles")
  else:
    print("Scalene")