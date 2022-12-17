import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * (10**4+1)
for _ in range(n):
    num = int(input())
    arr[num] += 1
for i in range(1, 10**4+1):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)
# counting sort. => 숫자의 범위가 작을 때 주로 사용
# 숫자의 범위가 가장 큰 수를 기준으로 배열 만든다.
# 원소 값이 곧 인덱스이며, 등장하면 값을 +1 해준다.
# 마지막으로 인덱스가 처음부터 끝까지 값이 0보다 크다면 index * arr[index] 즉, 값의 개수 만큼 출력하면 
# 배열이 정렬되었음을 알 수 있음.