def solution(n,a,b):
    # 1~n 토너먼트 게임
    # a번 참가자와 b번 참가자가 몇 번째 라운드에서 만나는지
    
    # a,b 참가자는 서로 붙게 되기 전까지 항상 이긴다
    # n은 항상 2의 지수승이므로 부전승은 없다
    
    # 매 라운드마다 a,b의 이름이 바뀌게 되는데 a홀수+1 = b짝수 가 되는지 체크
    
    if a > b: # 항상 a가 b보다 작다고 가정
        a,b = b,a
        
    round = 1
    while True:
        if a%2==1 and a+1 == b:
            return round
        if a%2 == 1: a += 1
        a //= 2
        if b%2 == 1: b += 1
        b //= 2
        round += 1
