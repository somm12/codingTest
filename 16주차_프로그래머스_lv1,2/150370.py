def cal(day):
    year, month, date = map(int, day.split('.'))
    return date + month * 28 + year * 28 * 12
    
def solution(today, terms, privacies):
    result = []

    dic = dict()
    for term in terms:
        k, v = term.split()
        dic[k] = int(v) * 28

    for i in range(len(privacies)):
        datetime, category = privacies[i].split()
        if cal(datetime) + dic[category] <= cal(today):
            result.append(i+1)

    return result
# 개인정보 수집 유효기간.
# 일수를 계산해서 비교연산으로 답을 구할 수 있다.