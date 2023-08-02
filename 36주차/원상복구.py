n,k = map(int,input().split())
S = list(map(int,input().split()))
D = list(map(int,input().split()))

for _ in range(k):
    new = [0]*n
    for i,v in enumerate(D):
        new[v-1] = S[i]
    S = new

for v in S:
    print(v,end=' ')
# 백준 구현문제