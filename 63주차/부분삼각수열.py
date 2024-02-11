n = int(input())
arr = list(map(int,input().split()))
answer =0
arr.sort()
if n <=2:
    print(n)
else:
    for i in range(n-1):
        x,y = arr[i],arr[i+1]
        for j in range(n):
            z = arr[n-1-j]
            if x+y > z:
                answer = max(answer, n-1-j-i+1)

    print(answer)
# 정렬한 상태에서 제일 작은 x,y 두 수의 합이 제일 큰 z보다 크다면 삼각관계를 만족한다.
# for 중복을 통해 조건에 만족하는 지점의 수열 길이를 업데이트함.