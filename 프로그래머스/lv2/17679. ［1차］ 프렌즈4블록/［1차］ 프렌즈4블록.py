from collections import deque

def solution(m, n, board):
    new_board = []
    for i in range(m):
        new_board.append(list(board[i]))
        
    answer = 0
    q = deque()
    
    while True:
        # 지울 블록 찾기 (4개 블록 중 왼쪽 위 점 하나 좌표)
        for i in range(m-1):
            for j in range(n-1):
                if new_board[i][j] == '':
                    continue
                if new_board[i][j] != new_board[i][j+1]:
                    continue
                if new_board[i][j] != new_board[i+1][j+1]:
                    continue
                if new_board[i][j] != new_board[i+1][j]:
                    continue
                q.append((i,j))
        
        # 더 이상 지울 블록이 없으면 리턴
        if len(q) == 0:
            return answer

        # 지우기 작업, 지워진 블록 카운트
        dx = [0,0,1,1]
        dy = [0,1,0,1]
        while q:
            x,y = q.popleft()
            for i in range(4):
                if new_board[x+dx[i]][y+dy[i]] != '':
                    answer += 1
                    new_board[x+dx[i]][y+dy[i]] = ''
        # 블록 떨어트리기
        for i in range(m-1,1,-1):
            for j in range(n):
                if new_board[i][j] != '':
                    continue
                temp = i
                while temp > 0:
                    temp -= 1
                    if new_board[temp][j] != '':
                        new_board[i][j] = new_board[temp][j]
                        new_board[temp][j] = ''
                        break