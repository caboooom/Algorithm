def solution(order):
    answer = 0
    for o in order:
        if o.find("americano") != -1 or o == "anything":
            answer += 4500
        else:
            answer += 5000
    return answer