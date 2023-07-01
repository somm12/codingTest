n = int(input())
arr= list(map(int,input().split()))
B,C = map(int,input().split()) # 총감독 감시 가능 학생수, 부감독 감시 가능 학생수.
ans = 0
for v in arr:
    ans += 1 # 총감독은 오직 한명만 감시가능.
    v -= B
    if v > 0:# 총감독이 감시 가능한 학생수를 뺐을 때, 학생수가 남아있다면
        if v% C == 0: # (남은 학생 수) % C 나누어 떨어지면 몫만 더하기
            ans += (v//C)
        else:
            ans += (v//C) + 1 # 나머지가 있다면, +1.
print(ans)