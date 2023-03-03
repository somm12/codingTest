def distance(now, target):
    a = abs(now[0] - target[0])
    b = abs(now[1] - target[1])
    return a+b
def solution(numbers, hand):
    answer = ''
    dict = {1: [0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    
    l = [3,0]
    r = [3,2]
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            l = dict[i]
        elif i in [3,6,9]:
            answer += 'R'
            r = dict[i]
        else:
            d1 = distance(l,dict[i])
            d2 = distance(r,dict[i])
            if d1 < d2:
                answer += 'L'
                l = dict[i]
            elif d1 > d2:
                answer += 'R'
                r = dict[i]
            else:
                answer += hand[0].upper()
                if hand == 'left':
                    l = dict[i]
                else:
                    r = dict[i]
    return answer
# 키패드 누르기