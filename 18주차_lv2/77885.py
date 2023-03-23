def countOne(x):
    x = bin(x)[2:]
    tmp = 0
    cnt = 1
    for i in x[::-1]:
        if i == '1':
            tmp += 1
            cnt = max(cnt,tmp)
            
        else:
            break
    return cnt
    
def solution(numbers):
    answer = []
    for i in numbers:
        t = countOne(i)
        answer.append(2**(t-1)+i)
    return answer
# 2개 이하로 다른 비트

# 다른 풀이: 짝수면 +1 하면되고, 홀수면 뒤에서 부터 처음 나오는 0인 수(index)를 1로 바꾸고, 그 
# index+1 위치에 0을 대입한다. ex) 7은(0111)의 2개 이하로 다른 비트는 11인 1011이다.
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 ==0:
            answer.append(i+1)
        else:
            tmp = bin(i)[2:]
            tmp = list('0'+tmp)
            for idx in range(len(tmp)-1,-1,-1):
                if tmp[idx] == '0':
                    tmp[idx] = '1'
                    tmp[idx+1] = '0'
                    break
            tmp = '0b'+ ''.join(tmp)
            answer.append(int(tmp,2))
    return answer