test = int(input())

number = []
result = []

for _ in range(test):
    n = int(input())
    number.append(n)

for i in number:
    if i <= 5:
        P = [1, 1, 1, 2, 2]
        result.append(P[i-1])
    else:
        P = [1, 1, 1, 2, 2] + [0] * (i-5)
        for j in range(5, i):
            P[j] = P[j-2] + P[j-3]
        result.append(P[i-1])
    
for x in result:
    print(x)