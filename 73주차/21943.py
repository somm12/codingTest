n = int(input())
numbers = list(map(int,input().split()))
P,Q = map(int,input().split())
visited = [0]*n
answer = 0
def combination():# Q개만큼의 조합 구하기.
    tmp = []
    def dfs(start,res):
        if len(res) == Q:
            tmp.append(res)
            return
        for i in range(start,n):
            dfs(i+1,res+[i])
    dfs(1,[])
    return tmp

def calc(arr):
    global answer
    total = 1

    for a in arr:
        total *= sum(a)
    answer = max(answer,total)

def cut(arr):
    
    combiIdxs = combination()# 자르는 위치 1번 ~ 7번 사이. 조합 구하기.
    for comb in combiIdxs:
        prev = 0
        result = []
        
        for i in comb:
            tmp = arr[prev:i]
            result.append(tmp)
            prev =i
        result.append(arr[comb[-1]:])# 마지막 번째 까지 자르고, 뒤에 남은 배열도 추가.
        calc(result)# 계산하기.

def perm(res):# 순열 구하기
    if len(res) == n:
        cut(res)# 자르기
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(res + [numbers[i]])
            visited[i] = 0

if P == 0:# 만약 덧셈연산자가 없다면 다 곱하기
    answer = 1
    for v in numbers:
        answer *= v
    print(answer)
elif Q == 0:# 만약 곱셈연산자가 없다면 다 더하기
    print(sum(numbers))
else:# 연산자가 모두 1개 이상씩 있다면 계산 시작.
    # 순열 구하기
    # 해당 순열에서 곱셈 연산자 개수인 Q개 만큼 자르기. 그러면 Q+1개 만큼 덩어리가 나옴. => 덧셈한 덩어리끼리 곱하기.
    # 자른 덩어리 끼리는 더하고 나머지는 모두 곱하면 값이 나옴.
    # 위의 값들 중 최대를 구한다.
    perm([])
    print(answer)
    