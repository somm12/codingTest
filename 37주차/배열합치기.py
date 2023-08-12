n,m = map(int,input().split())
new = []
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()# 각 배열 먼저 정렬
B.sort()

a = 0# A 배열의 인덱스 역할
b= 0# B 배열 인덱스 역할
while 0<= a < len(A) and 0 <= b < len(B):# 더 작은 값 부터 넣기.
    if A[a] < B[b]:
        new.append(A[a])
        a += 1
    else:
        new.append(B[b])
        b += 1
# 위의 while문에서 A,B 둘 중 하나의 배열 값은 모두 넣은 상태.
# ex) 1,2,3 vs 4,5,6 라면 B에 아직 값을 넣지 못함. 그래서 남은 값들은 추가하는 과정 필요.

while a < len(A):# 혹시 아직 추가하지 않은 값이 남았다면 마저 추가
    new.append(A[a])
    a += 1

while b < len(B):# 혹시 아직 추가하지 않은 값이 남았다면 마저 추가
    new.append(B[b])
    b += 1
for v in new:
    print(v,end=' ')
# 백준 투포인터 알고리즘 문제
# 두 가지 포인터 역할을 하는 변수를 가지고 주어진 문제를 해결함.