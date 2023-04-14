def calc(a,b):
    t1 = 0
    t2 = 0# 라이언
    for i in range(11):
        if a[i] > b[i]:
            t1 += (10-i)
        elif a[i] < b[i]:
            t2 += (10-i)
        elif a[i] == b[i] and a[i] == 0:
            continue
        elif a[i] == b[i] and a[i] != 0:
            t1 += (10-i)
    return t2-t1
def solution(n,info):
    ans = []
    arr = []
    def dfs(L,total):
        if L == 11:
            if total < n:
                arr[10] = n-total

            diff = calc(info,arr)
            if diff <= 0:
                ans.append([-1]+arr)
            else:
                ans.append([diff]+arr)
            
            return
        
        if total + info[L]+1 <= n:
            arr.append(info[L]+1)
            dfs(L+1,total+info[L]+1)
            arr.pop()
        arr.append(0)
        dfs(L+1,total)
        arr.pop()
    dfs(0,0)
    
    ans.sort(key=lambda x: (-x[0],-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1],-x[0]))
    
    if ans[0][0] == -1:
        return [-1]
    return ans[0][1:]