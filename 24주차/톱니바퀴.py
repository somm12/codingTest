from collections import deque

def move():
    rotate[n-1] = d
    if n == 1:# 1번 바퀴일 때
        if one[2] != two[6]:
            rotate[1] = -d
        if rotate[1] != 0:
            if two[2] != th[6]:
                rotate[2] = rotate[1]*-1
        if rotate[2] != 0:
            if th[2] != four[6]:
                rotate[3] = rotate[2]*-1
    elif n == 2:# 2번 바퀴 일때
        if two[6] != one[2]:
            rotate[0] = -d
        if two[2] != th[6]:
            rotate[2] = -d
        if rotate[2] != 0:
            if th[2] != four[6]:
                rotate[3] = rotate[2] * -1
    elif n == 3:# 3번 바퀴일때
        if th[2] != four[6]:
            rotate[3] = -d
        if th[6] != two[2]:
            rotate[1] = -d
        if rotate[1] != 0:
            if two[6] != one[2]:
                rotate[0] = -rotate[1]
    elif n == 4:# 4번 바퀴일때
        if four[6] != th[2]:
            rotate[2] = -d
        if rotate[2] != 0:
            if th[6] != two[2]:
                rotate[1] = -rotate[2]
        if rotate[1] != 0:
            if two[6] != one[2]:
                rotate[0] = -rotate[1]

one = deque(list(map(int,list(input()))))
two = deque(list(map(int,list(input()))))
th = deque(list(map(int,list(input()))))
four = deque(list(map(int,list(input()))))
k = int(input())
for _ in range(k):
    rotate = [0]*4
    n,d = map(int,input().split())
    move()
    # 회전
    one.rotate(rotate[0])
    two.rotate(rotate[1])
    th.rotate(rotate[2])
    four.rotate(rotate[3])
answer = one[0]+ (two[0]*2)**1 + (th[0]*2)**2 + (four[0]*2)**3
print(answer)