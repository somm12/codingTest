from itertools import combinations
def solution(orders, course):
    answer = []
    dict = {}
    max_num = {}
    
    for i,v in enumerate(orders):
        v = list(v)
        v.sort()
        orders[i] = ''.join(v)
    for order in orders:
        for n in range(2, len(order)+1):
            for i in list(combinations(list(order),n)):
                
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1
    for key, value in list(dict.items()):
        if not len(key) in max_num:
            max_num[len(key)] = value
        else:
            max_num[len(key)] = max(max_num[len(key)],value)
    for key,value in list(dict.items()):
        if value == max_num[len(key)] and value >=2 and len(key) in course:
            answer.append(''.join(list(key)))
    answer.sort()
        
    return answer
# 메뉴 리뉴얼