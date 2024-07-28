n,L = map(int,input().split())
g = []
newG = [[] for _ in range(n)]
for _ in range(n):
    g.append(list(map(int,input().split())))

for j in range(n):
    for i in range(n):
        newG[j].append(g[i][j])# 대칭으로 만들기 => 행만 체크해도 되는 로직으로 통일시키기 가능.

answer = 0


def sol(g):
    global answer
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if g[i][j] == g[i][j+1]: cnt +=1
            elif g[i][j]+1 == g[i][j+1] and cnt >= L: cnt = 1
            elif g[i][j]-1 == g[i][j+1] and cnt >= 0: cnt = -L + 1
            else: break
      
        else:# break가 되지 않고,
            if j == n-2 and cnt >=0: # 끝까지 반복문을 돌았고, 내리막 오르막 통과했다면!
                answer += 1
    
        
sol(g)
sol(newG)
       
print(answer)
# 백준 경사로.