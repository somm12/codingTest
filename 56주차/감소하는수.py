n = int(input())
ans = []
def dfs(L,res):
    if L > 10:
        return
    if len(res) > 0:
        ans.append(int(res))
    
    for i in range(10):
        if L > 0:
            if i < int(res[L-1]):# 이전 수 보다, 숫자가 작아야함
                dfs(L+1, res+str(i))
        else:
            dfs(L+1,str(i))

dfs(0,'')
ans.sort()# 정렬.
if n >= 1023: # 최대 1023개까지 만들 수 있음(9876543210)
    print(-1)
else:
    print(ans[n])
