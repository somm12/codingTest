n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

A = A[k:]
B = B[:k]
print(sum(A)+sum(B))
# 이코테 정렬 예제 3번