from collections import deque
n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr = deque(arr)
robot = deque([0]*n)
step = 1
while True:
    arr.rotate(1)
    robot.rotate(1)
    if robot[n-1] == 1:# 이전 단계에서 이동을 못했을 때의 경우, 내리는 위치로 이동될 수 있으니 즉시 내림.
        robot[n-1] = 0
    # 순서대로 로봇이동시키기.
    for i in range(n-2,-1,-1):
        if robot[i] == 1:
            if arr[i+1] > 0 and robot[i+1] == 0:
                robot[i+1] =1
                robot[i] = 0
                arr[i+1] -= 1
                if arr[i+1] == 0:
                    k -= 1
                if i + 1 == n - 1:# 내리는 위치로 이동했다면 즉시 로봇 내림.
                    robot[n-1] = 0
    if arr[0] > 0:# 올리는 위치에 로봇 올리기
        robot[0] = 1
        arr[0] -= 1
        if arr[0] == 0: # 혹시 올린 위치 내구도가 0이 되면 k -=1
            k -= 1
    if k <= 0:
        break
    step += 1
print(step)