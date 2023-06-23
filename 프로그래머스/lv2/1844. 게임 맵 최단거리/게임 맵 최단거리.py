from collections import deque
def solution(maps):
    answer = 0

    dx, dy = [-1,0,1,0], [0,1,0,-1]
    
    row = len(maps)
    col = len(maps[0])
    visited = [[0 for j in range (col)] for i in range(row)]
    
    q = deque()
    q.append((0,0))
    #table[0][0] = 1
    while q:
        x, y = q.popleft()
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<col and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y]+1
                
    if maps[row-1][col-1] > 1:
        return maps[row-1][col-1]
    return -1