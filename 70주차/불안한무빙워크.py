from collections import deque

n,k = map(int,input().split())
arr = deque()
people = deque([0]*(n))

for v in list(map(int,input().split())):
    arr.append(v)

def rotate():
    global arr,people
    arr.rotate(1)
    people.rotate(1)
    if people[n-1] == 1:# 1~3번 과정 중에 n번칸에 사람이 있다면 즉시 내림!
        people[n-1] = 0
def move():
    global arr,people
    for i in range(n-2,-1,-1):
        if people[i] == 1 and people[i+1] == 0 and arr[i+1] > 0:
            people[i] = 0
            people[i+1] = 1
            arr[i+1] -= 1
    if people[n-1] == 1:# 1~3번 과정 중에 n번칸에 사람이 있다면 즉시 내림!
        people[n-1] = 0

def first():# 첫번째 칸에 아무도 없고 안정성도 괜찮다면 올리기.
    global arr, people
    if people[0] == 0 and arr[0] > 0:
        people[0] = 1
        arr[0] -= 1

def isFinish():# 안정성이 0인 칸이 k개이상이면 종료.
    cnt = 0
    for v in arr:
        if v == 0:
            cnt += 1
    return cnt >= k

nth = 1
while True:
    rotate()

    move()
 
    first()
   
    if isFinish():
        print(nth)
        break
 
    nth += 1
