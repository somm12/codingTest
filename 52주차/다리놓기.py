import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    tmp  =1
    for _ in range(n):
        tmp *= m
        m -= 1
    for i in range(n,0,-1):
        tmp //= i
    print(tmp)
# 다리가 겹치지 않도록 다리 세우기
# mCn 구하기.
# 백준 조합 문제