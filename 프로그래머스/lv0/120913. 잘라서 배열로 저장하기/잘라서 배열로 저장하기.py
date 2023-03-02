def solution(my_str, n):
    answer = []
    idx = 0
    while idx < len(my_str):
        answer.append(my_str[idx:idx+n])
        idx += n
    return answer