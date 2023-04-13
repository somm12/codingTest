from collections import defaultdict
from bisect import bisect_left
def solution(info, query):
    answer= []
    dict = defaultdict(list)
    
    for i in info:
        a,b,c,d,e = i.split()
        e = int(e)
        for x1 in [a,'-']:
            for x2 in [b,'-']:
                for x3 in [c,'-']:
                    for x4 in [d,'-']:
                        dict[(x1,x2,x3,x4)].append(e)
    for i in list(dict.keys()):
        dict[i].sort()
    
    for i in query:
        i = i.replace("and ",'')
        a,b,c,d,e = i.split()
        score = int(e)
        if (a,b,c,d) in dict:
            x = bisect_left(dict[(a,b,c,d)],score)
            answer.append(len(dict[(a,b,c,d)]) - x)
        else:
            answer.append(0)
    return answer