from collections import deque
def solution(s):
    answer = True
    q = deque()
    for i in s:
        if i == "(":
            q.append(i)
        else:
            if len(q) == 0:
                return False
            q.pop()

    return True if len(q) == 0 else False