from collections import deque
n,k = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0]*n)

step = 1
while True:
    belt.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[n-1] = 0
    for i in range(n-1,-1,-1):
        if robot[i] == 1:
            if i == n-1:
                continue
            else:
                if robot[i+1] == 0 and belt[i+1] > 0:
                    belt[i+1] -=1
                    if belt[i+1] == 0:
                        k -=1 
                    robot[i+1] = 1
                    robot[i] = 0
    if belt[0]>0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            k -= 1
   
    if k <= 0:
        break
    step +=1
    
print(step)
# deque는 rotate를 사용해서 회전 가능하다.