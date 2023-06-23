def solution(s):
    answer = []

    zero = 0
    cnt = 0
    while True:
        if s == "1":
            return [cnt, zero]
        cnt += 1
        zero += int(s.count("0")) # 0을 제거
        s = bin(int(s.count("1")))[2:] # 2진 변환