n,k = map(int,input().split())
cnt = 0
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            
            tmp = time.count(str(k))
            
            if tmp >0:
                
                cnt += 1

print(cnt)
# k 가 하나라도 포함 되는 모든 시각 세기!
# 시각에 몇 개의 k개 있는가 아님.