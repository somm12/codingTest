import sys


def solution():
    global answer
    for i in range(n):# i,j로 먼저 안나 눈사람 쌍을 정하기.
        for j in range(i+3,n):
            s,e = i+1,j-1 # i,j 기준으로 그 뒤, 그 앞 부분 부터 시작하여 차이를 구한다.
            
            while s < e:
                tmp = (arr[s]+arr[e]) - (arr[i]+arr[j])
                if answer > abs(tmp):
                    answer = abs(tmp)
                
                elif tmp == 0:
                    answer = 0
                    return
                if tmp > 0:
                    e -= 1
                
                else:
                    s += 1

n = int(input())
arr = list(map(int,input().split()))
answer = sys.maxsize
arr.sort()# 정렬을 통해서 차이의 최솟값을 찾는다 -> 최솟값이 0 보다 커진다면, e를 줄이고, 0보다 작다면, l을 증가시켜서 범위를 좁혀나감.
solution()
print(answer)