from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    prior = deque(priorities)
    
    answer = 0
    while q:
        if q[0][0] == max(prior):
            num, idx = q.popleft()
            prior.remove(num)
            answer += 1
            if idx == location:
                return answer
        else:
            q.append(q.popleft())
            
    return answer