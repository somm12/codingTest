import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
# 멀쩡한 사각형 