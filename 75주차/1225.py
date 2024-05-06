a,b = input().split(" ")
a = list(map(int,list(a)))
b = list(map(int,list(b)))

dictA = {}
dictB = {}
for v in a:
    if v in dictA:
        dictA[v] += 1
    else:
        dictA[v] = 1
for v in b:
    if v in dictB:
        dictB[v] += 1
    else:
        dictB[v] = 1     
answer = 0

for keyA in dictA:
    for keyB in dictB:
        answer += (keyA * keyB* (dictA[keyA]*dictB[keyB]))
print(answer)
# 최대 자리수가 만개 이므로, 딕셔너리 사용해서, 중복된 조합 처리.