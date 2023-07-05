def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    # 1명 또는 2명씩 태우기
    a = 0
    b = len(people)-1
    while a <= b:
        if people[a] + people[b] <= limit:
            b -= 1
        a += 1
        answer += 1
    
    return answer