def solution(x):
    s = sum(list(map(int,str(x))))
    return True if x % s == 0 else False