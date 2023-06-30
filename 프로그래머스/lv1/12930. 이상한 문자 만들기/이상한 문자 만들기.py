def solution(s):
    answer = ''
    # 각 단어의 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자
    
    temp = s.split()
    
    blank = [0]*(len(temp)+1)
    idx=0
    for i in s:
        if i == ' ':
            blank[idx] += 1
        else:
            if blank[idx] > 0:
                idx += 1
    
    idx=0
    if s[0] == ' ':
        answer += ' '*blank[idx]
        idx += 1
        
    for word in temp:
        for i in range(len(word)):
            if i%2==0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        
        answer += ' '*blank[idx]
        idx += 1
        
    return answer