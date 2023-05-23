# SWEA 문제 - view 
for t in range(10):
    answer = 0
    n = int(input())
    arr = []
    arr = list(map(int,input().split()))

    for i in range(2, n-2):
        left = 0
        h1 = arr[i-1]
        h2 = arr[i-2]
        if h1 < arr[i] and h2 < arr[i]:
            left = arr[i] - max(h1,h2)
        right = 0
        h3 = arr[i+1]
        h4 = arr[i+2]
        if h3 < arr[i] and h4 < arr[i]:
            right = arr[i] - max(h3,h4)
        answer += min(left,right)

    print('#{} {}'.format(t+1,answer))
# 좌우로 조망권이 확보된 세대수 구하기.