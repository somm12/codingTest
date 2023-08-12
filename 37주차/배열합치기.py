n,m = map(int,input().split())
new = []
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

a = 0
b= 0
while 0<= a < len(A) and 0 <= b < len(B):
    if A[a] < B[b]:
        new.append(A[a])
        a += 1
    else:
        new.append(B[b])
        b += 1

while a < len(A):
    new.append(A[a])
    a += 1

while b < len(B):
    new.append(B[b])
    b += 1
for v in new:
    print(v,end=' ')
# 백준 투포인터 알고리즘 문제
# 두 가지 포인터 역할을 하는 변수를 가지고 주어진 문제를 해결함.