import math
def solution(fees, records):
    answer = []
    cal = {}
    car = {}
    fee = {}
    for i in records:
        t,num,io = i.split(" ")
        if num in car:
            car[num] +=1
        else:
            car[num] = 1
    for i in range(len(records)):
        t,n,io=records[i].split(" ")
        if car[n]%2 != 0:
            records.append("23:59 "+ n +" OUT")
            car[n] += 1

    for i in records:
        t,n,io = i.split(" ")
        time = list(map(int,t.split(":")))
        if n not in cal:
            cal[n] = time
        else:
            total = (time[0] - cal[n][0])*60 + (time[1] - cal[n][1]) 
            if n in fee:
                fee[n] += total
            else:
                fee[n] = total
            del(cal[n])
    for c in car.keys():
        if fees[0] < fee[c]:
            tmp = fees[1] + math.ceil((fee[c] - fees[0])/fees[2])*fees[3]
            fee[c] = tmp
        else:
            fee[c] = fees[1]
    a = list(fee.items())
    a.sort()
    for i in a:
        answer.append(i[1])
    return answer
# 주차 요금 계산