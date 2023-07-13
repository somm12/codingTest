from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
step = 1 # 종료되는 단계를 저장할 변수.

belt = deque(list(map(int,input().split()))) # 벨트 내구성도를 담을 큐.
robot = deque([0]*n)# 로봇이 존재함을 나태나는 큐. (0과 1로 표현)

def robotMove():# 로봇 이동.
    global belt
    for i in range(n-1,-1,-1):
        if robot[i]:
            if i+1>=n: # 마지막 칸이면
                robot[i] = 0# 즉시 내림
            else:
                if robot[i+1] or belt[i+1] <= 0: # 다음 칸이 내구성이 0 이하고, 다른 로봇이 있으면 그대로.
                    continue
                else:
                    robot[i+1] = 1
                    robot[i] = 0
                    belt[i+1] -= 1
def robotUp():# 올리는 위치에 로봇 올림.
    global robot,belt
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -=1
def isDone():# 내구성이 0 인 칸이 k개이상이면 종료.
    cnt = belt.count(0)
    if cnt >= k:
        return True
    return False

while True:
    # 벨트가 로봇과 함께 한 칸 씩 움직인다.
    belt.rotate(1)
    robot.rotate(1)
    robot[0] = 0 # 내리는 위치 칸에 있던 로봇은 즉시 내림. 첫 칸으로 이동 되기에 0으로 할당.
    robotMove() # 로봇 이동.
    robotUp()# 로봇 올리기.
    if isDone():
        print(step)
        break
    step +=1
