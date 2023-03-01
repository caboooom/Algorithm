def solution(num, k):
    nstr = str(num)
    return nstr.index(str(k))+1 if str(k) in nstr else -1