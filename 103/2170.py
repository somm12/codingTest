# n = int(input())
# arr =[]
# for _ in range(n):
#     a,b = map(int,input().split())
#     arr.append([a,b])
# arr.sort()
# answer = 0
# tmp = [arr[0]]
# for i in range(1,n):
#     s,e = tmp[-1]
#     ns,ne = arr[i]
#     if ns < e:
#         if e < ne:
#             tmp[-1][1] = ne
#     else:
#         tmp.append([ns,ne])
# for a,b in tmp:
#     answer += (b-a)
# print(answer)


n = int(input())
arr =[]
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort()
answer = 0
l,r = arr[0]# 가장 최근을 반영한 합쳐진 선.

for i in range(1,n):
    nl,nr = arr[i]
    if r < nl:# 다음 선이 떨어져 있다면 이전까지 선의 길이를 더함.
        answer += (r-l)
        l,r = nl,nr
    else:# 겹치면 업데이트.
        if r < nr:
            r = nr
answer += r-l# 마지막 선 길이 더해줌.
    
print(answer)
# 백준 선 긋기. 라인 스위핑.
