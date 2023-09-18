n,k = map(int,input().split())
arr = list(map(int,input().split()))
answer =0
dict = {}

for v in arr:
    diff = k - v
    if diff in dict:
        answer += dict[diff]
    
    if v in dict:
        dict[v] += 1
    else:
        dict[v] = 1
print(answer)
# n크기는 10만.
# 두 수(배열에서 다른 위치에 있는)의 합이 K가 되는 경우의 수 모두 구하기
# 딕셔너리를 이용해서 k-element가 존재하는지 확인.