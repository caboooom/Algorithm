def solution(chicken):
    coupon = chicken
    answer=0
    while coupon >= 10:
        answer += coupon//10 #쿠폰으로 주문
        coupon = coupon%10 + coupon//10 #남은쿠폰 + 새로발행된쿠폰
    
    return answer