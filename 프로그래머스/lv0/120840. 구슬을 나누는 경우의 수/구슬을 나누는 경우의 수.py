def factorial(x):
    if x<=1:
        return 1
    return x * factorial(x-1)


def solution(balls, share):
    answer = factorial(balls) // (factorial(share)* factorial(balls-share))
    return answer