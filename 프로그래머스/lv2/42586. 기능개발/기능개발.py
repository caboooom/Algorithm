def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    complete = [0]*n # progress별 배포일 기록
    check = 0 # 배포 완료된 progress 개수
    days = 1 # 경과 일수
    while check < n: # 모두 배포 완료될 때까지 반복
        for i in range(n):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                complete[i] = days
                check += 1
        days += 1
    
    # 차례대로 배포
    prev = complete[0]
    idx = 1
    cnt = 1
    while idx < n:
        if complete[idx] <= prev:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            prev = complete[idx]
        idx += 1
    if cnt > 0:
        answer.append(cnt)
        
    return answer