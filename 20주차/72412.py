import bisect, itertools, collections

def solution(info, query):
    infomap = collections.defaultdict(list)
    
    binarys = list(itertools.product((True, False), repeat=4))
    print(binarys)
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))
    print(infomap)
    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers
# 순위 검색
# collections.defaultdict(list)을 사용하면 if not in dict등 dict에 key value를
# 할당할 때 if문을 쓰지 않고도 바로 할당이 가능하다.
# query는 10만, 배열 원소는 최대 5만개 가능하므로, 시간 복잡도를 줄이기 위해
# 이진탐색을 활용하여. nlogn 시간 복잡도를 만드는 것이 중요하다.