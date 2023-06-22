def solution(msg):
    answer = []
    mydict = list("0ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    idx = 0
    temp = 0
    prev=''
    cur = msg[idx]
    while idx+1 <= len(msg)-1:
        if prev != '':
            mydict.append(prev+cur)
        next = msg[idx+1]

        # 현재 입력이 사전에 있으면, 인덱스를 기억해두고 입력에 다음 글자 추가
        if cur in mydict:
            temp = mydict.index(cur)
        while True:
            next = msg[idx+1]
            if cur + next in mydict:
                cur += next
                idx += 1
                if idx >= len(msg)-1:
                    break
                next = msg[idx]
                temp = mydict.index(cur)
            else:
                next = msg[idx+1]
                break
                
        ## 마지막 입력값에 대한 처리 ##
        if idx >= len(msg)-1:
            if cur in mydict:
                answer.append(mydict.index(cur))
            else:
                answer.append(len(mydict)+1)
            break
        
        # 기억해둔 인덱스 가지고 색인번호 출력
        answer.append(temp)

        # 현재 입력값 update
        prev=cur
        if idx+1 <= len(msg)-1:
            cur = msg[idx+1]
        idx += len(cur)

    ## 마지막 한 글자 남았을 경우 처리 ##
    if len(cur) == 1:
        if cur in mydict:
            answer.append(mydict.index(cur))
        else:
            answer.append(len(mydict)+1)

    return answer