from collections import deque

n,k = map(int,input().split())
belt = list(map(int,input().split()))

belt = deque(belt)
people = deque([0]*n)

answer = 1

def rotate():
    global belt,people
    people.rotate(1)
    belt.rotate(1)
    if people[n-1] == 1:# n번 칸이면 즉시 내림
        people[n-1] = 0

def move():
    global belt, people
    for i in range(n-2,-1,-1):
        if people[i] == 1:
            if people[i+1] == 0 and belt[i+1] > 0:
                people[i+1] = 1
                belt[i+1] -= 1
                people[i] = 0
    if people[n-1] == 1:# n번 칸이면 즉시 내림
        people[n-1] = 0
    
def add():
    global people, belt
    if people[0] == 0 and belt[0] > 0:
        people[0] = 1
        belt[0] -= 1

def check():
    cnt = 0
    for v in belt:
        if v == 0:
            cnt += 1
    return cnt >= k
                
while True:
    rotate()
    move()
    add()
    if check():
        break
    answer += 1
print(answer)
