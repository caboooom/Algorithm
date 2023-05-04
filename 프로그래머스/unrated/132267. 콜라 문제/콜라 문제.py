def solution(a, b, n):
    answer = 0
    cokes = n
    while cokes >= a:
        newcokes = (cokes//a)*b
        cokes = cokes%a + newcokes
        answer += newcokes
    return answer