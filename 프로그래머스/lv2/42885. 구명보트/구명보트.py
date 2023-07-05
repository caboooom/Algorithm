def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    # 1명 또는 2명씩 태우기
    idx = 0
    while idx < len(people):
        if people[idx] + people[-1] <= limit:
            people.pop()
        idx += 1
        answer += 1
    
    return answer