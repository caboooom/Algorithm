def solution(s):
    
    result = 0
    
    idx = 0
    while idx < len(s):
        cnt_x = 1 # 첫글자 x 같은수
        cnt_diff = 0 # 다른수
        
        cur = s[idx]
        idx += 1
        while idx < len(s):
            if cur == s[idx]:
                cnt_x += 1
            else:
                cnt_diff += 1
            if cnt_x == cnt_diff:
                idx += 1
                break
            idx += 1
        result += 1
        
    return result