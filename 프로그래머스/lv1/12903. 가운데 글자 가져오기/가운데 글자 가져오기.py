def solution(s):
    slen = len(s)
    if slen % 2 == 0:
        return s[slen//2-1:slen//2+1]
    else:
        return s[slen//2]