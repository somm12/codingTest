n = int(input())
m = int(input())
arr = list(map(int,input().split()))

dict = {}
for i,num in enumerate(arr):
    if num in dict:# 이미 게시 된 것은 추천 횟수 증가.
        dict[num][1] += 1
    else:# 게시 된 적이 없음.
        if len(dict) < n:# 공간 남았을 때.
            dict[num] = [num,1,i]
        else: # 공간이 없다면, 삭제 후 추가
            tmp = list(dict.values())
            
            tmp.sort(key = lambda x : (x[1],x[2]))# 추천 횟수가 작고, 게시된지 오랜된 순서로 삭제.
            deleteNum = tmp[0][0]# 삭제할 번호.
            del dict[deleteNum]
            
            # 새로 추가.
            dict[num] = [num,1,i]

res = list(dict.keys())
res.sort()
for v in res:# 오름차순 정렬.
    print(v,end=' ')