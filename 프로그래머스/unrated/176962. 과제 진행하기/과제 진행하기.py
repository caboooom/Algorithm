from collections import deque
def solution(plans):
    answer = []
    plans = sorted(plans,key = lambda x : (x[1])) # 시간 오름차순으로 정렬
    q = deque()
    n = len(plans)
    
    next = 1
    cur_time = plans[0][1]
    cur_task = plans[0]
    while len(answer) < n:
        ## 1. 할 일 정하기
        if cur_time == plans[0][1]:
            pass
        # 1-1. 지금이 다음플랜 시작시간이라면 바로 다음플랜을 시작
        elif next < n and plans[next][1] == cur_time:
            cur_task = plans[next]
            next += 1
            
        # 1-2. 하다 만 과제가 남아 있는지 큐에서 체크
        elif len(q) > 0:
            if next >= n: # 남은 다음 플랜이 없다면
                # 큐에 있는거 다 수행 후 종료
                while q:
                    answer.append(q.pop()[0])
                break
            else:
                # 큐에서 꺼낸 과제 시작
                cur_task = q.pop()
        
        # 1-3. 하던 과제가 없다면, plans에서 꺼낸 과제를 시작
        else:
            if next < n:
                cur_task = plans[next]
                next += 1

        ## 2. 현재 과제가 끝나는 시간 계산하기
    
        # 2-1. 다음 플랜이 남아 있지 않다면, 시간 생각하지 않고 진행
        if next >= n:
            answer.append(cur_task[0])
            continue

        # 2-2. 시간 계산
        else:
            # 큐에서 꺼낸 과제에 대해, 현재시간 update
            if cur_time < cur_task[1]:
                cur_time = cur_task[1]
            # 시간 계산
            curh , curm = map(int,cur_time.split(":"))
            curm += int(cur_task[2])
            if curm >= 60:
                endh = curh + curm//60
                endm = curm%60
            else:
                endh = curh
                endm = curm
            
            ## 3. 과제를 끝낼 수 있는지 판단
            # 3-1. 현재 과제를 끝낼 수 없는 경우, 큐에 넣고 현재 시간 update 해주기
            if str(endh).zfill(2)+":"+str(endm).zfill(2) > plans[next][1]:
                h1, m1 = map(int,plans[next][1].split(":"))
                h2, m2 = map(int,cur_time.split(":"))
                temp = int(cur_task[2])-((h1*60+m1) - (h2*60+m2))
                cur_task[2] = str(temp)
                cur_time = plans[next][1] # cur time update
                q.append(cur_task)
            # 3-2. 현재 과제를 끝낼 수 있는 경우, answer에 넣고 현재시간 update해주기
            else:
                answer.append(cur_task[0])
                cur_time = str(endh).zfill(2)+":"+str(endm).zfill(2)
    
    
    return answer