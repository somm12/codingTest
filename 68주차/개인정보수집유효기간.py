def solution(today, terms, privacies):
    answer = []
    ty,tm,td = map(int,today.split('.'))
    today = (ty*12*28) + (tm*28) + td
    dict = {}
    for s in terms:
        kind,v = s.split(' ')
        dict[kind] = int(v)
    for i,value in enumerate(privacies):
        day,kind = value.split(" ")
        duration  = dict[kind]*28
        ny,nm,nd = map(int,day.split('.'))
        time = (ny*12*28) + (nm*28) + nd
        if time + duration <= today:
            answer.append(i+1)
        
    answer.sort()
    return answer