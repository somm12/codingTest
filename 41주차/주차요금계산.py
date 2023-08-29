from collections import defaultdict
import math
def solution(fees, records):
    answer= []
    check = defaultdict(int) # 각 차량번호에 대해서 IN, OUT이 짝에 맞게 있는지 체크.
    time = defaultdict(int) # 해당 차량번호의 총 주차시간 담기(분)
    
    for s in records:
        arr =s.split()
        check[arr[1]] += 1 # 짝수면 짝에 맞게 있는 것.
  
    for num in check:
        if check[num] % 2 != 0:
            tmp = '23:59' + ' ' + num + ' ' + 'OUT' # 출차가 없다면 출차 표시 넣기.
            records.append(tmp)
    
    for s in records:
        t,num, io = s.split()
        h,m = t.split(":")
        tmp = int(h)*60 + int(m) # 입차, 출차한 시각을 분으로 만들기.
        if io == 'IN': # in이면 -붙여서 더함
            time[num] += -tmp
        else: # out이면 + 붙여서 총 주차한 시간을 구해나가기.
            time[num] += tmp
  
    for num in time: 
        if time[num] <= fees[0]:# 주차시간이 기본 주차 시간이하라면 기본요금 청구
            answer.append((num,fees[1]))
        else:
            total = fees[1] # 기본 주차시간을 넘으면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구.
            total += (math.ceil((time[num]- fees[0])/fees[2])) * fees[3] # 올림 주의.
            answer.append((num, total))
    answer.sort()# 차량번호가 작은 순.
    
        
    return [v[1] for v in answer]

# 프로그래머스 카카오 문제.