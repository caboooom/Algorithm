def solution(babbling):
    answer = 0
    for word in babbling:
        if word in ["aya","ye","woo","ma"]:
            answer += 1
            continue
        flag = True
        idx = 0
        while idx < len(word):
            if word[idx:idx+2] in ["ye", "ma"]:
                if idx >= 2:
                    if word[idx-2:idx] == word[idx:idx+2]:
                        flag = False
                        break
                idx += 2
            elif word[idx:idx+3] in ["aya","woo"]:
                if idx >= 3:
                    if word[idx-3:idx] == word[idx:idx+3]:
                        flag = False
                        break
                idx += 3
            else:
                flag = False
                break
        if flag == True:
            answer += 1
                
    return answer