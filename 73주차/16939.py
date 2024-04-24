n,m = map(int,input().split())
people = []
for _ in range(n):
    people.append(list(map(int,input().split())))


answer = 0

def getSum(arr):
    total = 0
    for i in range(n):
        maxV = 0
        for num in arr:
            maxV = max(maxV, people[i][num])
        total += maxV
    return total

def combi(start,res):# 치킨 3개 조합 구하기.
    global answer
    if len(res) == 3:
        answer = max(answer,getSum(res))# 시킨 치킨 종류 중에서 각 사람의 선호도가 가장 큰 것. 만족도의 총 합을 구하기.
        return
    for i in range(start, m):
        combi(i+1, res+[i])

combi(0,[])
print(answer)
# 치킨치킨치킨 문제