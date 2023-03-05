def solution(survey, choices):
    answer = ''
    d = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(choices)):
        score = abs(choices[i]-4)
        if 5 <= choices[i] <= 7:
            d[survey[i][1]] += score
        else:
            if choices[i] != 4:
                d[survey[i][0]] += score
    if d['R'] >= d['T']:
        answer += 'R'
    else:
        answer += 'T'
    if d['C'] >= d['F']:
        answer += 'C'
    else:
        answer += 'F'
    if d['J'] >= d['M']:
        answer += 'J'
    else:
        answer += 'M'
    if d['A'] >= d['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
# 아래는 딕서녀리 key에 문자열("RT":1 와 같은 )을 넣은 형태로,zip 라이브러리를 이용하여
# 더 빠른 풀이를 만들 수 있다.
# zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 
# 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환한다.
def solution(survey, choices):
    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}# 왼쪽에 위치한 성격유형을 음수 점수,오른쪽은 양수 점수로 가정.
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():# 순서가 바껴서 "TR" 와 같이 나올 수 있음을 방지.
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
# 성격 유형 검사하기