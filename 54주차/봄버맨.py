import sys
input = sys.stdin.readline
R,C,N = map(int,input().split())
g = []

dx =[-1,1,0,0]
dy = [0,0,-1,1]
for i in range(R):
    g.append(list(input().rstrip()))

if N == 1:
    for x in range(R):
        for y in range(C):
            print(g[x][y],end='')
        print()
elif N % 2 == 0:
    for _ in range(R):
        for _ in range(C):
            print('O',end='')
        print()
else:
    bombs1 = [['O']*C for _ in range(R)]# 3,7,11, =>4로 나누어 3이 나머지인 경우.
    # 초기 폭탄들과, 인접한 부분이 폭발된 모습.
    for x in range(R):
        for y in range(C):
            if g[x][y] == 'O':
                bombs1[x][y] = '.'
            else:
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0<= nx < R and 0 <= ny < C and g[nx][ny] == 'O':
                        bombs1[x][y] = '.'
                        break
    # 5,9,13, => 4로 나누어 1이 나머지인 경우
    # bombs1의 상태에서 폭탄들이 폭발한 경우.
    bombs2 = [['O']*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if bombs1[x][y] == 'O':
                bombs2[x][y] = '.'
            else:
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0<= nx < R and 0 <= ny < C and bombs1[nx][ny] == 'O':
                        bombs2[x][y] = '.'
                        break
    if N % 4 == 1:
        for x in range(R):
            for y in range(C):
                print(bombs2[x][y],end='')
            print()
    if N % 4 == 3:
        for x in range(R):
            for y in range(C):
                print(bombs1[x][y],end='')
            print()
# 백준 문제