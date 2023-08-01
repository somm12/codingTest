s = input()

r,c = int(s[1]), ord(s[0])-96
answer =0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

route = [[3,3,1],[3,3,0],[2,2,1],[2,2,0],
[0,0,2],[0,0,3],[1,1,2],[1,1,3]]

for arr in route:
    nx,ny = r,c
    for d in arr:
        nx += dx[d]
        ny += dy[d]
        if 1 <= nx <= 8 and 1<= ny <= 8:
            continue
        else:
            break
    else:
        print(arr)
        answer += 1
print(answer)