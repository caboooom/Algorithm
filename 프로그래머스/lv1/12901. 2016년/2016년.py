def solution(a, b):
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [0,31,29,31,30,31,30,31,31,30,31,30]
    totalday = sum(month[:a]) + b
    return days[totalday%7]