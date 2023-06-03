def solution(s):
    answer = []
    s = s.strip("{}")
    lst = s.split("},{")
    lst.sort(key = lambda x : (len(x)))

    for i in lst:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer