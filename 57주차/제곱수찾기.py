n,m =map(int,input().split())
A = []
for _ in range(n):
    A.append(list(input()))
answer = -1
def check(num):
    num = int(num)
    if num**0.5 == int(num**0.5):
        return True
    return False
    
for rd in range(-n,n):# 행과 열 등차 범위 지정.
    for cd in range(-m,m):
        if rd == 0 and cd == 0: continue# 둘다 0 일 때는 지나감.
        for sx in range(n):# 수열 시작점이 될 좌표.
            for sy in range(m):
                tmp = ''
                i,j = sx,sy
                while 0 <= i < n and 0 <= j < m:# 시작점 부터 ~ 지정한 등차 대로 합해진 수.
                    tmp += A[i][j]
                    i += rd
                    j += cd
                    if check(tmp):
                        answer = max(answer,int(tmp))
print(answer)