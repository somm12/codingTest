// js로 프로그래머스 풀기 - 고득점 kit 정렬.
function solution(citations) {
    var answer = -1;
    citations.sort();
    let maxV = Math.max(...citations);
    
    for (let i = maxV; i >=0 ;i--){
        let cnt = 0;
        for ( let j = citations.length-1 ; j >= 0;j--) {
            if ( i <= citations[j]) {
                cnt += 1
        }
        if ( cnt >= i) answer = Math.max(answer,i)
            
        }
    }
    return answer;
}