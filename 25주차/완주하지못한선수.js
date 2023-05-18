// 프로그래머스 고득점 kit 문제. JS로 풀기.
function solution(participant, completion) {
    var answer = '';
    let p = {}
    for (let i of participant){
        if (i in p) p[i] += 1
        else p[i] = 1
    }
    for (let i of completion) {
        if (i in p) p[i] -=1
    }
    
    for (let i of Object.keys(p)) {
        if (p[i] === 1) return i
    }
    return answer;
}