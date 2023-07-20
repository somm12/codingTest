from collections import deque
n,k = map(int,input().split())
step = 1

A = list(map(int,input().split()))
A = deque(A)

robot = deque([0]*n)

def moveRobot():
    global A, robot
    for i in range(n-2,-1,-1):
        if robot[i]:
            if robot[i+1] == 0 and A[i+1] > 0:
                robot[i+1] = 1
                A[i+1] -= 1
                robot[i] = 0
    if robot[-1]:
        robot[-1] = 0

def isDone():
    cnt = 0
    for v in A:
        if v == 0:
            cnt += 1
    if cnt >= k:
        return True
    return False

while True:
    A.rotate(1)
    robot.rotate(1)
    robot[0] = 0
    robot[-1] = 0

    moveRobot()

    if A[0] >0 :
        robot[0] = 1
        A[0] -= 1
    
    if isDone():
        break
    step += 1
print(step)