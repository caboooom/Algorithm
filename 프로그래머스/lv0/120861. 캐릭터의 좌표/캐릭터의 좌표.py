def solution(keyinput, board):
    xLimit = board[0]//2
    yLimit = board[1]//2
    
    x, y = 0, 0
    for key in keyinput:
        if key == "up":
            nx, ny = x, y+1
        if key == "down":
            nx, ny = x, y-1
        if key == "left":
            nx, ny = x-1, y
        if key == "right":
            nx,ny = x+1, y
            
        if -xLimit<=nx<=xLimit and -yLimit<=ny<=yLimit:
            x, y = nx, ny
    return [x,y]