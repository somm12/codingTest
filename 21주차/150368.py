from itertools import product
def solution(users, emoticons):
    answer = []
    for arr in list(product([10,20,30,40],repeat=len(emoticons))):
        cnt = 0
        sale= 0
        for d,p in users:
            total = 0
            for idx,v in enumerate(arr):
                if arr == (30,40):
                    print(idx,v)
                if d <= v:
                    total += (emoticons[idx] - (emoticons[idx]*(v/100)))
           
            if total >= p:
                cnt += 1
                total = 0
            sale += total
        answer.append((cnt,sale))
    answer.sort(key=lambda x:(-x[0],-x[1]))
        
    return answer[0]
# 이모티콘 할인행사