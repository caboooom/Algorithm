from fractions import Fraction
def solution(dots):
    x1,y1=dots[0]
    x2,y2=dots[1]
    x3,y3=dots[2]
    x4,y4=dots[3]
    
    if Fraction(x1-x2,y1-y2) == Fraction(x3-x4,y3-y4):
        return 1
    if Fraction(x1-x3,y1-y3) == Fraction(x2-x4,y2-y4):
        return 1
    if Fraction(x1-x4,y1-y4) == Fraction(x2-x3,y2-y3):
        return 1
    return 0