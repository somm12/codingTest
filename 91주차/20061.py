def gMove(t,x,y):
    
    if t == 1 or t == 3:
        for i in range(1,6):
            if i+1 >= 6 or green[i+1][y] == 1:
                green[i][y] = 1
                if t==3:
                    green[i-1][y] = 1
                break
    else:
        for i in range(1,6):
            if i+1 >= 6 or green[i+1][y] == 1 or green[i+1][y+1] == 1:
                green[i][y] = 1
                green[i][y+1] = 1
                
                break

def bMove(t,x,y):
    
    if t == 1 or t == 2:
        for j in range(1,6):
            if j+1 >= 6 or blue[x][j+1] == 1:
                blue[x][j] = 1
                if t==2:
                    blue[x][j-1] = 1
                break
    else:
        for j in range(1,6):
            if j+1 >= 6 or blue[x][j+1] == 1 or blue[x+1][j+1] == 1:
                blue[x][j] = 1
                blue[x+1][j] = 1
                
                break
def greenOrg(row):
    global green
    for j in range(4):
        green[row][j] = 0
    for i in range(row-1,-1,-1):
        for j in range(4):
            green[i+1][j] = green[i][j]
            green[i][j] = 0
   
def gRemove():
    global answer
    for i in range(2,6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1
        if cnt ==4:
            greenOrg(i)
            answer += 1
            
def blueOrg(col):
    global blue
    for i in range(4):
        blue[i][col] = 0
    for j in range(col-1,-1,-1):
        for i in range(4):
            blue[i][j+1] = blue[i][j]
            blue[i][j] = 0
    
        
def bRemove():# 꽉찬 열 개수 만큼, 그 전의 열이 당겨짐. -> 바로 사라지고 한 열씩 당기는 방식.
    global answer

    for j in range(2,6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt ==4:
            blueOrg(j)
            answer +=1   

def gCheck():
    
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                greenOrg(5)
                break

def bCheck():
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                
                blueOrg(5)
                break
answer = 0
green = [[0]*4 for _ in range(6)] 
blue = [[0]*6 for _ in range(4)]

n = int(input())
for _ in range(n):
    t,x,y = map(int,input().split())
    gMove(t,x,y)
    bMove(t,x,y)
    
    gRemove()# 한 행이 꽉차면, 제거
    bRemove()# 한 열이 꽉찬다면, 제거,
    
    gCheck()# 연한 블록에 값이 있다면 맨 아래 행 또는 열 제거.
    bCheck()

total = 0
# 남은 블록 개수.
for i in range(2,6):
    for j in range(4):
        total += green[i][j]

for j in range(2,6):
    for i in range(4):
        total += blue[i][j]
print(answer)
print(total)
# 백준 모노미노도미노2.
        
    