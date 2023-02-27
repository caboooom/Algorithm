def solution(num_list, n):
    answer = []
    idx = 0
    for i in range(len(num_list)//n):
        answer.append(num_list[idx:idx+n])
        idx+=n
    return answer