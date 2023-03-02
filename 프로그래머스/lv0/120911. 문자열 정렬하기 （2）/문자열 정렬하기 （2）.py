def solution(my_string):
    answer = []
    for str in my_string:
        answer.append(str.lower())
    return ''.join(sorted(answer))