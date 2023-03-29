def solution(seoul):
    n = 0
    for x in seoul:
        if x == "Kim":
            break
        n += 1
    return "김서방은 {}에 있다".format(n)