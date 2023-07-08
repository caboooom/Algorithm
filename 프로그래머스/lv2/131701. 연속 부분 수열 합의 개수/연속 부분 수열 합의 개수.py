def solution(elements):
    n = len(elements)
    temp = set()
    for i in range(1,n+1):
        a = 0
        for j in range(n):
            if a+i < n:
                temp.add(sum(elements[a:a+i]))
            elif a + i == n:
                temp.add(sum(elements[a:]))
            else:
                temp.add(sum(elements[a:]) + sum(elements[:a+i-n]))
            a += 1
    return len(temp)