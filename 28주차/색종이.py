arr = [[0]*100 for _ in range(100)]
n = int(input())
answer =0
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j]:
            answer += 1

print(answer)
# 100 x 100 도화지에서 해당하는 범위 부분에 1을 넣는 방법으로, 넓이에 해당하는 부분을 만듦.
# 1의 개수가 곧 검은 종이 개수