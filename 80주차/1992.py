n = int(input())

g = []
for _ in range(n):
    g.append(list(input()))

def dfs(x,y,L):
    cnt = ''
    num = set()
    for i in range(x,x+L):
        for j in range(y,y+L):
            num.add(g[i][j])
    if len(num)==2:
        v= L//2
        cnt += dfs(x,y,v)
        cnt += dfs(x,y+v,v)
        cnt += dfs(x+v,y,v)
        cnt += dfs(x+v,y+v,v)
    else:
        if '1' in num:
            return '1'
        return '0'
    return '(' + cnt + ')'
print(dfs(0,0,n))
# 1 또는 0으로만 이뤄지면 값만 반환, 아니면 4등분해서 대표 값 찾아서 반환. -> 재귀
# 백준 쿼드트리.

