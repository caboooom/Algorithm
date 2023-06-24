def check(string):
    stack = []
    for i in string:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            top = stack.pop() 
            if top+i not in ["()", "[]", "{}"]:
                return 0
    if len(stack) > 0:
        return 0
    return 1

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        answer += check(s[i:] + s[:i])
    return answer