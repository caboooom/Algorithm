def solution(n, lost, reserve):
    students = [0]*(n+1) # 학생 번호는 1부터 시작
    
    # 잃어버린 학생이 여벌체육복 가지고 있는 경우
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    for i in range(1,n+1):
        if i not in lost:
            students[i] = 1
        else:
            if i-1 in reserve: # 이전 학생
                reserve.remove(i-1)
                students[i] = 1
            elif i+1 in reserve: # 다음 번호 학생
                reserve.remove(i+1)
                students[i] = 1
    answer = students.count(1)
    return answer