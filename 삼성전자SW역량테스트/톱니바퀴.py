arr = []
for _ in range(4):
    arr.append(list(map(int,input())))
k = int(input())

def rotate(nth,d):
    signal = [0]*4
    signal[nth-1] = 1
    di = [0]*4
    di[nth-1] = d

    for i in range(nth-1,0,-1):
        if arr[i][6] != arr[i-1][2] and signal[i] == 1:
            signal[i-1] =1
            di[i-1] = di[i] * -1
    for i in range(nth-1,3):
        if arr[i][2] != arr[i+1][6] and signal[i] == 1:
            signal[i+1] = 1
            di[i+1] = di[i]*-1
    for i in range(4):
        if signal[i] == 1:
            if di[i] == -1:
                arr[i] = arr[i][1:] + [arr[i][0]]
            else:
                arr[i] = [arr[i][-1]] + arr[i][:-1]

for _ in range(k):
    nth, direction = map(int,input().split())
    rotate(nth,direction)

# 점수구하기
ans = 0

for i in range(4):
    if arr[i][0] == 1:
        ans += 2**i
print(ans)