from collections import deque
def solution(maps):
    answer = 0
    # 벽은 지나갈 수 없음
    # 미로를 빠져나가는 문의 레버를 경유해서 출구로 가야함.
    # 지나갔던 길을 또 지날 수 있음.
    # 한 칸에 1초
    # 탈출할 수 없으면 -1을 리턴
    
    row = len(maps)
    col = len(maps[0])
    
    # 출발점, 레버, 출구 위치 찾기
    q = deque()
    sx, sy, lx, ly, ex, ey = 0,0,0,0,0,0
    for i in range(row):
        if "S" in maps[i]:
            sx = i
            sy = maps[i].index("S")
        if "L" in maps[i]:
            lx = i
            ly = maps[i].index("L")
        if "E" in maps[i]:
            ex = i
            ey = maps[i].index("E")
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    # 레버까지 bfs -> visited 초기화 -> 출구까지 bfs
    
    visited = [[0 for j in range(col)] for i in range(row)]
    count = [[0 for j in range(col)] for i in range(row)]
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        if maps[x][y] == "L":
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<col:
                if maps[nx][ny] != "X":
                    q.append((nx,ny))
                    count[nx][ny] = count[x][y] + 1
    cnt = count[lx][ly]
    
    if cnt == 0:
        return -1
    
    # visited 초기화
    for i in range(row):
        for j in range(col):
            visited[i][j] = 0
            count[i][j] = 0
    # q 초기화
    q.clear()
    
    q.append((lx,ly))
    while q:
        x, y = q.popleft()
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        if maps[x][y] == "E":
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<col:
                if maps[nx][ny] != "X":
                    q.append((nx,ny))
                    count[nx][ny] = count[x][y] + 1
    cnt += count[ex][ey]
    
    if visited[ex][ey] == 0:
        return -1
    return cnt