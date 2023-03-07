def rotate(arr):
    n, m = len(arr), len(arr[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

def check(newLock):
    length = len(newLock)//3
    for i in range(length,length*2):
        for j in range(length,length*2):
            if newLock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    newLock = [[0 for j in range(n*3)] for i in range(n*3)]
    for i in range(n,n*2):
        for j in range(n,n*2):
            newLock[i][j] = lock[i-n][j-n]
            
    #key를 4번 회전시키면서 확인
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠 껴보기
                for i in range(m):
                    for j in range(m):
                        newLock[x+i][y+j] += key[i][j]
                #열리는지 체크
                if check(newLock) == True:
                    return True
                #자물쇠 빼기
                for i in range(m):
                    for j in range(m):
                        newLock[x+i][y+j] -= key[i][j]
                    
    return False