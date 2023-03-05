def solution(A, B):
    if A==B:
        return 0
    
    answer = 0
    for i in range(len(A)-1):
        answer += 1
        A = A[-1]+A[:-1]
        if A == B:
            return answer
        
    return -1