a, b = input().split()
n1, n2 = list(a), list(b)
print(max( ''.join(reversed(n1)), ''.join(reversed(n2)) ))