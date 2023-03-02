def solution(participant, completion):
    dict = {}
    for i in completion:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    for i in participant:
        if i in dict:
            dict[i] -= 1
        else:
            return i
    for i in dict:
        if dict[i] < 0:
            return i
# 완주하지 못한 선수 : 해시 이용(딕셔너리)

# Counter 라이브러리를 이용한 간략한 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Counter 생성자에 문자열을 인자로 넘기면 각 문자가 문자열에서 
# 몇 번씩 나타나는지를 알려주는 객체가 반환됨.ex) Counter({'leo': 1, 'kiki': 1, 'eden': 1})
# 뺄셈을 통해 각 객체에서 값이 존재하는지 확인을 쉽게 할 수 있다.