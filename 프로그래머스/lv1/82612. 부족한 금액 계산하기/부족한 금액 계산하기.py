def solution(price, money, count):
    cost = 0
    for i in range(1,count+1):
        cost += price * i
    answer = money - cost
    if answer > 0 :
        return 0
    else:
        return -answer