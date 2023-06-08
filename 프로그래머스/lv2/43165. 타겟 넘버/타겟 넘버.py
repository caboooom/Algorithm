def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        temp = []
        for parent in leaves:
            temp.append(parent + num)
            temp.append(parent - num)
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer