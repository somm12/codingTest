R,C,N = map(int,input().split())
g = []
for _ in range(R):
    g.append(list(input()))
bomb1 = [['O']*C for _ in range(R)]# 경우 1
bomb2 = [['O']*C for _ in range(R)]# 경우 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]

if N % 2 == 0:# 짝수 번째는 항상 폭탄이 모두 설치된 상태.
    for x in range(R):
        for y in range(C):
            print(bomb1[x][y],end ='')
        print()
elif N == 1:# 첫 1초동안은 아무일도 없음.
    for x in range(R):
        for y in range(C):
            print(g[x][y],end ='')
        print()
else:# 다음 일초. 동안 3초전에 폭탄이 폭발.(3초, 7초, 11초 ,,,, 이 때는 초기상태에서 폭탄이 폭발한것과 같음.)
    for x in range(R):
        for y in range(C):
            if g[x][y] == 'O':
                bomb1[x][y] = '.'
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0 <= nx < R and 0 <= ny < C:
                        bomb1[nx][ny] = '.'
   
    for x in range(R):# (5초, 9초, ,,, 이 경우에는 앞전에 홀수 번째 상태에서 폭탄이 폭발한 것과 같음.)
        for y in range(C):
            if bomb1[x][y] == 'O':
                bomb2[x][y] = '.'
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0 <= nx < R and 0 <= ny < C:
                        bomb2[nx][ny] = '.'
                

    if N%4 == 3:# 3이 나머지인 경우는 bomb1.
        for x in range(R):
            for y in range(C):
                print(bomb1[x][y],end ='')
            print()
    elif N%4 == 1:# 1이 나머지인 경우는 bomb1가 터지고 난 후의 상태인 bomb2
        for x in range(R):
            for y in range(C):
                print(bomb2[x][y],end ='')
            print()