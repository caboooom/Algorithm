
def solution(new_id):
    answer = ''
    
    temp = ''
    for x in new_id:
        if temp == "" and x == ".":
            continue
        if x.isalpha():
            temp += x.lower()
        elif x.isdigit():
            temp += x
        else:
            if x in "-_.":
                temp += x
    
    for i in range(len(temp)):
        if temp[i] == ".":
            if i<len(temp)-1 and temp[i+1] == ".":
                continue
        answer += temp[i]
    
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[:-1]
        
    if len(answer) == 0:
        return "aaa"
    
    if len(answer) >= 16:
        answer = answer[:15]
    
    if answer[-1] == ".":
        answer = answer[:-1]
        
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
        
    return answer