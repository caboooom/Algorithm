def solution(brown, yellow):
    answer = []
    
    y1 = yellow # 노란색 영역 가로 길이
    y2 = 1 # 노란색 영역 세로 길이
    while True:
        if (y1+y2)*2 + 4 == brown:
            break
        else:
            temp = y2 + 1
            while temp * (yellow//temp) != yellow:
                temp += 1
            y2 = temp
            y1 = yellow//y2
        
    return [y1+2, y2+2]