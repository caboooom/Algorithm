from collections import deque
def solution(plans):
    answer = []
    plans = sorted(plans,key = lambda x : (x[1]))
    q = deque()
    n = len(plans)
    
    next = 1
    cur_time = plans[0][1]
    cur_task = plans[0]
    while len(answer) < n:
        ## 1. 할 일 정하기
        
        if cur_time == plans[0][1]:
            pass
        # 다음플랜 시작시간이라면 바로 다음플랜을 시작
        elif next < n and plans[next][1] == cur_time:
            cur_task = plans[next]
            next += 1
            
        # 큐를 먼저 체크
        elif len(q) > 0:
            if next >= n: # 다음 플랜이 없다면
                # 큐에 있는거 다 수행
                while q:
                    answer.append(q.pop()[0])
                break ############
            else:
                # 큐에서 꺼낸 과제 시작
                cur_task = q.pop()
        
        # 또는 plans에서 꺼낸 과제를 시작
        else:
            if next < n:
                cur_task = plans[next]
                next += 1

    # 2. 끝나는 시간 계산하기
    
    # plans 다음 일이 없다면 그냥 진행하기
        if next >= n:
            answer.append(cur_task[0])
            continue

    # plans의 다음 일 시작시간보다 늦게 끝나면 playtime을 update하고, 큐에 넣기
        else:
        # 일이 끝나는 시간 계산
            if cur_time < cur_task[1]:
                cur_time = cur_task[1]
            #temph, tempm = map(int, cur_task[1].split(":"))
            curh , curm = map(int,cur_time.split(":"))
            
            curm += int(cur_task[2])
            if curm >= 60:
                endh = curh + curm//60
                endm = curm%60
            else:
                endh = curh
                endm = curm
        
        # 끝내기에 시간이 부족하면   
            if str(endh).zfill(2)+":"+str(endm).zfill(2) > plans[next][1]:
                h1, m1 = map(int,plans[next][1].split(":"))
                h2, m2 = map(int,cur_time.split(":"))
                temp = int(cur_task[2])-((h1*60+m1) - (h2*60+m2))
                cur_task[2] = str(temp)
                cur_time = plans[next][1] # cur time update
                q.append(cur_task)
        #그렇지 않으면 answer에 넣고 현재시간 update해주기
            else:
                answer.append(cur_task[0])
                cur_time = str(endh).zfill(2)+":"+str(endm).zfill(2)
    
    
    return answer