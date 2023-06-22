def solution(s):
    # 문자열은 알파벳 소문자
    # 문자열에서 같은 알파벳 두개가 연속해질때마다 그 둘을 제거
    
    stack = []
    for i in s:
        if len(stack)>0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        return 1
    if len(stack)%2 != 0:
        return 0
    while len(stack)>0:
        if stack.pop() != stack[-1]:
            return 0
        stack.pop()