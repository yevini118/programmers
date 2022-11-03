import math

def solution(w,h):
    
    square = w*h #총 사각형의 개수
    gcd = math.gcd(w,h) #최대공약수
    
    w //= gcd #가장 작은 단위 사각형의 w
    h //= gcd #가장 작은 단위 사각형의 h
    
    return square - (w + h - 1)*gcd