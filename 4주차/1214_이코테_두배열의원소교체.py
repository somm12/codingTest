n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
# 제일 작은 원소 A에서 k개, 큰 원소를 B에서 k개를 비교하기 위해서 정렬.
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
# 이미 정렬이 되어 있기 때문에, A원소가 B의 원소보다 크다면 더이상 원소의 합을 크게 만들 수 없고,
# 비교하지 않아도 되서 break로 탈출.