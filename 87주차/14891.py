from collections import deque

arr = [[]]
for _ in range(4):
    tmp = list(map(int,list(input())))
    arr.append(deque(tmp))
k = int(input())

def move(num,di):
    global arr
    check = [0]*5 # i번 톱니바퀴가 회전하는지 체크할 배열
    d = [1]*5 # i번 톱니바퀴가 회전하는 방향을 저장. (1: 시계, -1: 반시계)
    check[num] = 1
    d[num] = di
    
    for i in range(num+1,5):# num번 톱니바퀴기준 오른쪽에 있는 바퀴 체크
        if arr[i-1][2] == arr[i][6]:# 맞물리는 부분 극이 같으면 바로 그만!
            break
        else:
            check[i] = 1
            d[i] = d[i-1]*-1 # 이전 바퀴와 반대 방향을 가진다.
            
    for i in range(num-1,0,-1):# num번 톱니바퀴기준 왼쪽에 있는 바퀴 체크
        if arr[i+1][6] == arr[i][2]:# 맞물리는 부분 극이 같으면 역시 바로 그만.
            break
        else:
            check[i] = 1
            d[i] = d[i+1]*-1
    
    for i in range(1,5):
        if check[i]:
            arr[i].rotate(d[i])
   
def getScore():
    global answer
    for i in range(1,5):# 각 번호에 따라서 2의 제곱임.
        answer += (arr[i][0] * (2**(i-1)))# 점수 계산 => 12시 방향은 0번 값이고, 해당 값이 1이여야 점수를 획득가능함.
       
for _ in range(k):
    num, direct = map(int,input().split())
    move(num,direct)
  

answer= 0
getScore()
print(answer)
# 백준 톱니바퀴.