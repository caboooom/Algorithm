import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int,input().split()))
v = int(input())

print(nlist.count(v))