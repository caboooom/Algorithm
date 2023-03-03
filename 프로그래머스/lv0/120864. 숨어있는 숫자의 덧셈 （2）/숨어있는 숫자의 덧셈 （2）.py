def solution(my_string):
    result = ''
    for str in my_string:
        if str.isalpha():
            result += ' '
        else:
            result += str
    arr= result.split(' ')
    answer=0
    for i in arr:
        if i.isdigit():
            answer += int(i)
    return answer