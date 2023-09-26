dict = {}
nth = 1
def solution(word):
   
    def dfs(res):
        global dict,nth
        if len(res)>=1:
            dict[res] = nth
            nth+=1
        if len(res) == 5:
            return
        for v in ['A','E','I','O','U']:
            dfs(res+v)
    dfs('')
    return dict[word]
# 프로그래머스 완전탐색.
# 모음 사전 문제.