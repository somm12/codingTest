h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
# 모두 초로 바꾸기.
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2

if t2 > t1:
    t = t2-t1
else:# 값이 t2가 더 작다면, 24시간 더하기.
    t = 24*60*60 + t2-t1
# 시간 분 초로 변환.
h = t//60//60
m = t//60 % 60
s = t % 60
print("%02d:%02d:%02d"%(h,m,s))