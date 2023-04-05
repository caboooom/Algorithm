def solution(s, n):
    answer = ''
    for x in s:
        if x == " ":
            answer += " "
        elif x.isupper():
            if ord(x) + n <= 90:
                answer += chr(ord(x)+n)
            else:
                answer += chr(ord(x)+n-26)
        elif x.islower():
            if ord(x) + n <= 122:
                answer += chr(ord(x)+n)
            else:
                answer += chr(ord(x)+n-26)
    return answer