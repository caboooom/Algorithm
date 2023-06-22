def solution(dirs):
    table = [[0 for i in range(11)] for j in range(11)]
    move = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}
    
    # 원점 : 5,5
    x = 5
    y = 5
    
    # 캐릭터가 지나간 좌표 순서대로 구하기
    visited = [(5,5)] 
    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1] # 이동좌표
        if 0 <= nx <= 10 and 0 <= ny <= 10: # 범위체크
            visited.append((nx,ny))
            x, y = nx, ny

    # 처음 걷는 길 count
    line = [(visited[i], visited[i+1]) for i in range(len(visited)-1)]
    answer = 0
    check = []
    for a,b in line:
        if (a,b) not in check and (b,a) not in check:
            answer += 1
            check.append((a,b))
    
    return answer