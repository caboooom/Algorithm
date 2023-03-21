def solution(board, moves):
    answer = 0
    
    n = len(board)
    
    after = []
    for i in range(len(moves)):
        cur_pos = moves[i] - 1
        for j in range(n):
            if board[j][cur_pos] != 0:
                after.append(board[j][cur_pos])
                board[j][cur_pos] = 0
                break
                
    if len(after)<=1:
        return 0

    if len(after)==2 and after[0]==after[1]:
        return 2
    
    result=[]
    idx = 1
    while idx < len(after):
        if after[idx] == after[idx-1]:
            result.append(after.pop(idx))
            result.append(after.pop(idx-1))
            if idx == 1:
                idx = 0
            else:
                idx -= 2
        idx += 1
        
    return len(result)