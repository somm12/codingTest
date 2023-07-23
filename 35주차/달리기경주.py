def solution(players, callings):
    answer = []
    dict = {}
    for i,v in enumerate(players):
        dict[v] = i
        
    for name in callings:
        nowIndex= dict[name]
        prevName = players[nowIndex-1]
        
        dict[name] -= 1
        dict[prevName] += 1
        players[nowIndex] = prevName
        players[nowIndex -1] = name
        
    return players
# 프로그래머스 문제