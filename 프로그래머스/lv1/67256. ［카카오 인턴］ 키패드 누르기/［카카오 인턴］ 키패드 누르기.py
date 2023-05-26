def solution(numbers, hand):
    answer = ''
    
    location = dict()
    for i in range(1,13):
        location[i] = [(i-1)//3, (i-1)%3]
    
    left = 10
    right = 12
    
    for i in numbers:
        if i == 0:
            i = 11
        if i in [1,4,7]:
            answer += "L"
            left = i
        elif i in [3,6,9]:
            answer += "R"
            right = i
        else:
            # 거리 계산
            ldist = abs(location[left][0] - location[i][0]) + abs(location[left][1] - location[i][1])
            rdist = abs(location[right][0] - location[i][0]) + abs(location[right][1] - location[i][1]) 
            
            # 키패드 누를 손가락 결정
            if ldist > rdist:
                answer += "R"
                right = i
            elif ldist == rdist:
                if hand == "right":
                    answer += "R"
                    right = i
                else:
                    answer += "L"
                    left = i
            else:
                answer += "L"
                left = i

    return answer