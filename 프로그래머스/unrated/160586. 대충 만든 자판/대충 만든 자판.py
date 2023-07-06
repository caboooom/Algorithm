def solution(keymap, targets):
    answer = []
    
    key_dict = dict()
    for key in keymap:
        for i in range(len(key)):
            k = key[i]
            if k not in key_dict:
                key_dict[k] = i+1
            else:
                key_dict[k] = min(key_dict[k], i+1)
    
    for target in targets:
        cnt = 0
        for ch in target:
            if ch not in key_dict:
                cnt = -1
                break
            cnt += key_dict[ch]
        answer.append(cnt)
    return answer