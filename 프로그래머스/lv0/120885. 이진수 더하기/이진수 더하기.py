def solution(bin1, bin2):
    b1, b2 = int(bin1,2), int(bin2,2)
    sum = str(bin(b1+b2))
    return sum[2:]