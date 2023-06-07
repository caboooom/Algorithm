import math
from collections import deque

def calc_time(car, carnum, out_h, out_m):
    in_h, in_m = int(car[carnum][0]), int(car[carnum][1])
    return (out_h*60 + out_m) - (in_h*60 + in_m)

def solution(fees, records):
    answer = dict()
    car = dict()
    q = deque()
    for info in records:
        h, m, carnum, state = info.replace(":"," ").split()
        h, m, carnum = map(int,[h, m, carnum] )
        if state == "IN":
            car[carnum] = (h,m)
            q.append(carnum)
        else:
            if carnum not in answer:
                answer[carnum] = calc_time(car, carnum, h, m)
            else:
                answer[carnum] += calc_time(car, carnum, h, m)
            q.remove(carnum)
            
    while q:
        carnum = q.popleft()
        if carnum not in answer:
            answer[carnum] = calc_time(car, carnum, 23, 59)
        else:
            answer[carnum] += calc_time(car, carnum, 23, 59)
            
    for i in answer:
        if answer[i] <= fees[0] :
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + math.ceil((answer[i]-fees[0])/fees[2]) * fees[3]
    answer = sorted(answer.items())
    return [i[1] for i in answer]