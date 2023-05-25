n,m,k = map(int,input().split())
A = []
# 3차원 배열. x,y 칸에 나무들의 나이를 담음.
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    A.append(list(map(int,input().split())))
# 나무 m개 입력.
for _ in range(m):
    a,b,c = map(int,input().split())
    tree[a-1][b-1].append(c)
# 8방향.
dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]
# 처음에 nxn 칸에 모두 5만큼 양분 존재.
feed = [[5]*n for _ in range(n)]

def spring(): # 봄. 나이만큼의 양분을 먹고 나이가 + 1.
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                tree[x][y].sort() # 나이가 어린것부터 양분주기.
                dead = 0
                temp = []
                for age in tree[x][y]:
                    if age <= feed[x][y]: # 나이만큼의 양분이 존재한다면.
                        feed[x][y] -= age
                        age += 1
                        temp.append(age) # 살아있는 나무는 따로 담는다.
                    else:# 여름: 만약 나이보다 양분이 부족하면 죽은 나무들의 나이//2 만큼 양분 줌.
                        dead += (age//2)
                feed[x][y] += dead
                tree[x][y] = []
                tree[x][y].extend(temp) # 뒤에 배열을 합친다.

def fall(): # 가을. 나이가 5의 배수라면 8방향으로 나이가 1인 나무가 생성.
    for x in range(n):
        for y in range(n):
            for age in tree[x][y]:
                if age % 5 == 0:
                    for i in range(8):
                        nx = x+dx[i]
                        ny = y +dy[i]
                        if 0 <= nx < n and 0<= ny < n: # 범위 내에서 새로 생김.
                            tree[nx][ny].append(1) # 맨앞에 1를 추가하면 따로 정렬 필요 없음.
            feed[x][y] += A[x][y] # 겨울. for 중복문 내에서 겨울 처리가능.
for _ in range(k): # k년후.
    spring()
    fall()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j]) # x,y 칸에 남아있는 나무 개수를 구함.
print(answer)