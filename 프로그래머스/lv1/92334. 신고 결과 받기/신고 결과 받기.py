def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    
    counts = dict()
    for id in id_list:
        counts[id] = [set(),set()] # 내가신고한유저, 나를신고한유저
    stop = set()
    
    for r in report:
        user1, user2 = r.split()
        counts[user1][0].add(user2) 
        counts[user2][1].add(user1) 
        if len(counts[user2][1]) >= k:
            stop.add(user2)
            
    for i in range(len(id_list)):
        for user in counts[id_list[i]][0]:
            if user in stop:
                answer[i] += 1
    
    
    return answer