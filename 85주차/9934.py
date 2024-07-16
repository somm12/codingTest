k = int(input())
arr = list(map(int,input().split()))
n = 2**k - 1
answer = [[]for _ in range(n)]
def dfs(s,e,level):# 현재 범위의 중간이 곧, 해당 레벨의 노드.

    if s > e: return

    if s == e:
        answer[level].append(arr[s])
        return
    
    mid = (s+e)//2
    
    answer[level].append(arr[mid])
    dfs(s,mid-1,level+1)# 두 방향으로 나누기.
    dfs(mid+1,e,level+1)

dfs(0,n-1,0)

for i in range(k):
    for v in answer[i]:
        print(v,end =' ')
    print()

# 백준 완전 이진트리.