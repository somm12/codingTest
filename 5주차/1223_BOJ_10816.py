from bisect import bisect_left, bisect_right
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
arr.sort()

for x in a:
    print(bisect_right(arr, x) - bisect_left(arr,x),end=' ')

# 다른 풀이
from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = list(map(int,stdin.readline().split()))
index, m_dic = 0, {}

for m in sorted(M):
    cnt = 0
    if m not in m_dic:
        while index < len(N):
            if m == N[index]:
                cnt += 1; index += 1
            elif m > N[index]:
                index += 1
            else: break
        m_dic[m] = cnt

print(' '.join(str(m_dic[m]) for m in M))
# N이 이미 정렬 되어 있으므로, m이 첫 원소보다 작다면 존재하지 않는다는 아이디어를 가지고
# 문제를 풀 수 있다.

# 다른 풀이2
from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))
# count 메소드를 사용하여, 개수 세기 범위를 줄일 수 있다.
# 출처 https://chancoding.tistory.com/45