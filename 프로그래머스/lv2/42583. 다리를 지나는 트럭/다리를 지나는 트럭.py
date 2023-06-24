def solution(bridge_length, weight, truck_weights):
    # 다리에 완전히 오르지 않은 트럭의 무게는 무시함
    # 트럭이 다리를 건너는 순서는 정해져있음   
    
    time = 0
    bridge = [0 for i in range(bridge_length)]
    end = 0 # 다리를 모두 건넌 트럭 개수
    n = len(truck_weights)
    now = 0 # 현재 다리 위 트럭 무게 합
    
    while end < n:
        time += 1
        # 다리 위 트럭 앞으로 한칸씩 이동
        temp = bridge.pop(0)
        if temp > 0:
            end += 1
            now -= temp 
        bridge.append(0)
        # 다음 트럭 다리에 올릴 수 있으면 올리기
        if len(truck_weights)>0 and now +truck_weights[0] <= weight and bridge[-1] == 0:
            bridge[-1] = truck_weights.pop(0)
            now += bridge[-1]
    
    return time