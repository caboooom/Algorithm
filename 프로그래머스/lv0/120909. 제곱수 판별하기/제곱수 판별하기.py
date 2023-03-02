import math
def solution(n):
    a = math.sqrt(n)
    return 1 if a - int(a) == 0 else 2