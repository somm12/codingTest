from collections import defaultdict
n = int(input())
stu = defaultdict(list)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
seat = [[0]* n for _ in range(n)]
for _ in range(n**2):
    s = list(map(int,input().split()))
    for j in s[1:]:
        stu[s[0]].append(j)# stue = {1:[x,x,x,x],2:[x,x,x,x]} 1번 학생 : 1번 학생이 좋아하는 학생list
    
    


def like(arr):
    dict = defaultdict(list)
    for x in range(n):
        for y in range(n):
            if seat[x][y] == 0:# 남은 빈칸 중에서 후보 선택!!!!!!!!!!!
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny= y + dy[i]
                    if 0 <= nx < n and 0 <= ny <n:
                        if seat[nx][ny] in arr:
                            cnt += 1
                dict[cnt].append((x,y))
    a = list(dict.items())
    a.sort(key=lambda x : -x[0])
    return a[0][1]

def empty(can):
    dict = defaultdict(list)
    for x,y in can:
        cnt = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and seat[nx][ny] == 0: # 빈칸일때
                cnt += 1
        dict[cnt].append((x,y))
    a = list(dict.items())
    a.sort(key=lambda x : -x[0])
    a = a[0][1]
    # 빈칸이 여러개 있으면 행과 열이 더 작은 칸으로 배정
    if len(a) > 1:
        a.sort(key=lambda x:(x[0],x[1]))
        return a[0]
    return a[0]

def satisfy():
    total = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(4):
                nx = x+dx[i]
                ny= y + dy[i]
                if 0 <= nx < n and 0 <= ny <n:
                    if seat[nx][ny] in stu[seat[x][y]]:
                        cnt += 1
            if cnt == 0 or cnt == 1:
                total += cnt
            elif cnt == 2:
                total += 10
            elif cnt == 3:
                total += 100
            else:
                total += 1000
    return total

for num in stu:
    candidates = like(stu[num])
    if len(candidates) > 1:
        locate = empty(candidates)
        seat[locate[0]][locate[1]] = num
    else:
        seat[candidates[0][0]][candidates[0][1]] = num
answer = satisfy()
print(answer)
