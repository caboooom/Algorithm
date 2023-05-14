def solution(food):
    half = []
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            half.append(str(i))
    result = half + ['0'] + half[::-1] # 물은 항상 1개
    return ''.join(result)