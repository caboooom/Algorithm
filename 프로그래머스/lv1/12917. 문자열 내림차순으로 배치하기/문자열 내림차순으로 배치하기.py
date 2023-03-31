def solution(s):
    slist = list(s)
    slist.sort(reverse = True)
    return ''.join(slist)