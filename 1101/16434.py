n,atk = map(int,input().split())
arr  = []
for _ in range(n):
    t,a,h = map(int, input().split())
    arr.append((t,a,h))

def check(curHp):
    initAtk = atk 
    maxHp = curHp
    for t,a,h in arr:
        if t == 1:# 몬스터와 대결하는 경우.
            cnt = (h//initAtk) 
            if h % initAtk:
                cnt += 1
            cnt -= 1# 몬스터가 죽을 때 까지 몬스터가 공격하는 횟수
            curHp -= (cnt * a)
        else:# 포션일 경우.
            initAtk += a
            curHp += h
            if curHp > maxHp:# 최대hp를 넘길 수 없음.
                curHp = maxHp
            
        if curHp <= 0:# 0이하면 False.
            return False
    return True

s = 1
e = int(1e18) # 최대 100만 * 100만 * 123456.
ans = 1
while s<= e:
    mid = (s+e)//2
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(int(ans))
# 백준 드래곤 앤 던전 