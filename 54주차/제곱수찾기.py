n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(input()))

answer = -1# 완전 제곱수인 경우가 없다면 -1 반환.

for i in range(n):# 시작 행 좌표
    for j in range(m):# 시작 열 좌표
        for rd in range(-n,n):# 행의 등차 범위
            for cd in range(-m,m):# 열의 등차 범위
                num = ''
                x,y = i,j
                if rd == 0 and cd == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    num += A[x][y]
                    if int(num)**0.5 == int(int(num)**0.5):# 완전 제곱수인지 확인.
                        answer = max(answer,int(num))
                    x += rd
                    y += cd

print(answer)