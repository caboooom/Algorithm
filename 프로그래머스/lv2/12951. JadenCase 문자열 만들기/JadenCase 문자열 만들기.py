def solution(s):
    answer = []
    temp = s.split(" ")
    for i in temp:
        if i == "":
            answer.append("")
        else:
            answer.append(i[0].upper() + i[1:].lower())

    return " ".join(answer)