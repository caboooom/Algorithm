def solution(babbling):
    answer = 0
    dic=["aya","ye","woo","ma"]
    for b in babbling:
        temp=[0]*4
        bab=''
        for i in range(4):
            if dic[i] in b:
                temp[i] += 1
                bab += dic[i]
        if len(bab)==len(b) and [2,3,4] not in temp:
            answer += 1
    return answer