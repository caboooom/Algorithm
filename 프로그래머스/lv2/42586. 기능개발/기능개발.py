from collections import deque

def solution(progresses, speeds):
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    days = 0
    cnt = 0
    while progresses:
        if progresses[0] + days*speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            days += 1
    answer.append(cnt)
        
    return answer