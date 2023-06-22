def solution(book_time):
    answer = 0
    # 퇴실 후 청소시간 10분
    # 코니에게 필요한 최소 객실의 수를 리턴
    
    book_time.sort()
    rooms = ["00:00"] # 방마다 종료시간을 저장
    
    for time in book_time:
        start, end = time
        
        # 청소까지 완료한 시간 계산
        if int(end[3:]) <= 49:
            end = end[:3] + str(int(end[3:])+10)
        else:
            end = str(int(end[:2])+1).zfill(2) + ':' + str((int(end[3:])+10)%60).zfill(2)
        
        # 손님 받을 수 있는 객실이 있다면
        if start >= min(rooms):
            # update
            idx = rooms.index(min(rooms))
            rooms[idx] = end
        # 없으면 방 개수 늘리기
        else:
            rooms.append(end)  
    return len(rooms)
