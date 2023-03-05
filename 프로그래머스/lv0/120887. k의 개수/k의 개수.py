def solution(i, j, k):
    answer = 0
    itoj=''
    for num in range(i,j+1):
        itoj += str(num)
    return itoj.count(str(k))