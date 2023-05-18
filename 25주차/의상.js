// 프로그래머스 고득점 키트 문제 JS로 풀기.
function solution(clothes) {
    var answer = 0;
    dict = {}
    for ( let i =0; i < clothes.length ; i++){
        if (clothes[i][1] in dict) {
            dict[clothes[i][1]].push(clothes[i][0])
        }
        else dict[clothes[i][1]] = [clothes[i][0]]
    }
    answer = 1
    for (let i in dict){
        answer *= (dict[i].length+1)
    }
    return answer-1;
}
