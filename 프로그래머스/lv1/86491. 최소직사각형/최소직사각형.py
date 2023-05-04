def solution(sizes):
    width, length = 0, 0
    for x in sizes:
        if x[0] < x[1]:
            x[0], x[1] = x[1],x[0]
        width = max(width,x[0])
        length = max(length,x[1])
    return width*length