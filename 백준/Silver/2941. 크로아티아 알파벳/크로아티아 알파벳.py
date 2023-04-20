import sys
input = sys.stdin.readline

word = input().rstrip()

change_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in change_list:
  word = word.replace(x,'*')

print(len(word))