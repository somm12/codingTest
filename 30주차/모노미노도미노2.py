green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]

score = 0
n = int(input())

def greenMove(t,y): # 초록판쪽으로 범위 밖/ 다른 블록과 마주치기 전까지 움직이기
    global green
    r = 1
    if t == 1 or t==3 : # 1x1 or 2x1 라면,
        for _ in range(5):# while 써도 됨.
            if r+1>=6 or green[r+1][y] : # 다음 행부분에서 범위밖이나, 다른 블록과 마주칠 때.
                green[r][y]= 1 # 현재 행쪽에 블록 두기.
                
                if t==3: # 그게 2x1라면 세로 모양으로 되도록 배치
                    green[r-1][y] = 1
                break
            r += 1
            
    else: # 1x2 라면,
        for _ in range(5): # 다음 행부분에서 범위 밖 or 다른 블록과 마주친다면.
            if r+1 >= 6 or green[r+1][y] or green[r+1][y+1]:
                green[r][y] = 1
                green[r][y+1] = 1
                break
            r += 1
        
def blueMove(t,x): # 파란색 판으로 블록 움직이기.
    global blue
    c=1
    if t == 1 or t==2: #1x1,1x2
        for _ in range(5):
            if c+1>=6 or blue[x][c+1]: # 다음 열에서 블록이 있거나 범위가 넘어간다면, 할당.
                blue[x][c] = 1
                if t==2: # 1x2라면, - 모양으로 배치.
                    blue[x][c-1] = 1
                break
            c += 1
    else:# 2x1
        for _ in range(5): 
            if c+1>=6 or blue[x][c+1] or blue[x+1][c+1]:
                blue[x][c]=1
                blue[x+1][c] = 1
                break
            c+=1
        
def greenRemove(): # 혹시 한 행이 꽉 차있다면, 제거하고, 해당 행의 윗부분 모두 한 칸씩 아래로 이동.
    global score,green
    for i in range(2,6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1
        if cnt ==4: # 꽉 찼다면
            greenOrg(i) # 해당 행부분 위쪽은 아래쪽으로 한칸씩 이동.
            score += 1 # 점수 +1
def greenOrg(row): # 매개변수에 해당하는 행을 지우고 한칸씩 아래로이동시키는 함수.
    global green
    
    for i in range(row,0,-1):
        for j in range(4):
            green[i][j] = green[i-1][j]
    for j in range(4): # 마지막으로 이동하면 맨 위쪽 행은 값이 남아있어서 0으로 초기화.
        green[0][j] = 0
def blueRemove(): # 혹시 한 열이 꽉 차있다면, 제거하고, 해당 열의 왼쪽열 모두 한 칸씩 오른쪽으로 이동.
    global score,blue

    for j in range(2,6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt ==4:
            blueOrg(j)
            score +=1
def blueOrg(col): # 매개변수에 해당하는 열을 지우고 한칸씩 오른쪽으로 이동시키는 함수.
    global blue
    
    for j in range(col,0,-1):
        for i in range(4):
            blue[i][j] = blue[i][j-1]
            
    for i in range(4):# 마지막으로 이동하면 맨 왼쪽 행은 값이 남아있어서 모두 0으로 초기화.
        blue[i][0] = 0
        
def greenCheck(): # 점수 획득후, 혹시 0,1번 행에 블록이 담아있다면, 맨 아래쪽 행을 삭제, 한칸씩 아래로.
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                greenOrg(5)
                break
def blueCheck(): # 0,1 열 블록이 존재하면, 맨 오른쪽 열을 삭제, 한칸씩 오른쪽.
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                
                blueOrg(5)
                break
for _ in range(n):
    t,x,y = map(int,input().split())
    greenMove(t,y) # 각 보드로 이동.
    blueMove(t,x)
   
    greenRemove() # 꽉찬 열 / 행을 지우고 한칸씩 땡김.
    blueRemove()
   
    greenCheck() # 혹시 0,1번 행이나 열에 블록이 있다면 지우고 한 칸씩 땡김.
    blueCheck()

block = 0 
for i in range(6):
    for j in range(4):
        
        if green[i][j]:
            block += 1
    
for i in range(4):
    for j in range(6):
        
        if blue[i][j]:
            block += 1

# 총 점수와, 남은 블록수를 출력.
print(score)
print(block)