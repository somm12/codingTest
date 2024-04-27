import sys
input = sys.stdin.readline
n,k = map(int,input().split())

if k < 5:
    print(0)
else:
    arr = []
    answer =0
    for _ in range(n):
        arr.append(input())
    init = set()
    for v in ['a','n','t','i','c']:
        init.add(v)
    alpha = []
    for i in range(97,123):
        v = chr(i)
        if v not in init:
            alpha.append(v)
    
    def check(res):
        global answer 
        total =0
      
        for w in arr:
            for i in range(4, len(w)-4):
                if w[i] not in res:# 한 문자라도 없다면 해당 단어는 만들 수 없다.
                    break
            else:
                total += 1
        answer = max(answer,total)# 최댓값 업데이트.
    
    def dfs(start,res):
        if len(res) == k:# k개를 고르고 나면, 주어진 단어를 만들 수 있는지 체크.
            check(res)
            return
        for i in range(start,len(alpha)):
            dfs(i+1,res+ [alpha[i]])
    
    dfs(0,['a','n','t','i','c'])# 알파벳 고르기.
    print(answer)
# 가르침