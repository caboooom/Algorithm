def solution(dirs):
    table = [[0 for i in range(11)] for j in range(11)]
    move = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}
    
    # 원점 : 5,5
    x = 5
    y = 5
    
    visited = set() # 방문한 선분
    prev = (5,5)
    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1] # 이동좌표
        if 0 <= nx <= 10 and 0 <= ny <= 10: # 범위체크
            visited.add((prev,(nx,ny)))
            visited.add(((nx,ny),prev))
            prev = (nx,ny)
            x, y = nx, ny
    return len(visited)//2