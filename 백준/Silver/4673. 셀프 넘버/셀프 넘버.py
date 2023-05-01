
def self_num(n):
  result = n
  l = len(str(n))
  for i in range(l):
    result += n%10
    n //= 10
  return result


numbers = [i for i in range(1,10001)]

cur = 1
check = 1
while True:
  if check > 10000:
    break
  cur = self_num(cur)
  if cur in numbers:
    numbers.remove(cur)
  else:
    check += 1
    cur = check

for i in range(len(numbers)):
  print(numbers[i])