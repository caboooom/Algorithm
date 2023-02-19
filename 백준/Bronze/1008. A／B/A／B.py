 ### 1 ###
#a, b = map(float, input().split())
#print(round(a/b,9))

 ### 2 ###
#python은 정수 나눗셈 결과를 실수형으로 저장하므로 입력값을 int형으로 받아도 된다
#python은 나눗셈 할 때 오차 10^-9 이하로 계산해주기 때문에, round()를 쓰지 않아도 된다
a, b = map(int, input().split())
print(a/b)