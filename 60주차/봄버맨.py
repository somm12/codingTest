R,C,N = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
g= []
for _ in range(R):
    g.append(list(input()))

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

b1 = [['O']*C for _ in range(R)]
b2 = [['O']*C for _ in range(R)]
if N % 2 == 0:
    for arr in b1:
        print(''.join(arr))
else:
    if N == 1:
        for v in g:
            print(''.join(v))
    else:
        for x in range(R):
            for y in range(C):
                if g[x][y] == 'O':
                    b1[x][y] = '.'
                    for i in range(4):
                        nx,ny = x+dx[i],y+dy[i]
                        if inRange(nx,ny) and b1[nx][ny] == 'O':
                            b1[nx][ny] = '.'
        if N % 4 == 1:
            for x in range(R):
                for y in range(C):
                    if b1[x][y] == 'O':
                        b2[x][y] = '.'
                        for i in range(4):
                            nx,ny = x+dx[i],y+dy[i]
                            if inRange(nx,ny) and b2[nx][ny] == 'O':
                                b2[nx][ny] = '.'

        if N % 4 == 3:
            for arr in b1:
                print(''.join(arr))
        elif N % 4 == 1:
            for arr in b2:
                print(''.join(arr))
# 4초마다 주기가 있음.
# 3초, 7초에는 초기 버전에서 폭탄 터진 모습
# 5초, 9초 에는 이전 3초 때 모습, 7초 때 모습에서 폭탄이 터진 모습.