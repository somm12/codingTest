t1 = input()
t2 = input()

ht1,mt1,st1 = map(int,t1.split(":"))
ht2,mt2,st2 = map(int,t2.split(":"))

total = st1 + (mt1*60) + (ht1*60*60)
total2 = st2 + (mt2*60) + (ht2*60*60)

if total2 > total:
    v = total2 - total
else:# 최대 24시간 기다릴 수 있으므로, 주의.
    v = total2 - total + (24*60*60)
print("%02d:%02d:%02d" % (v//60//60, v//60%60, v%60))