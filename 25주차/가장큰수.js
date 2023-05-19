//프로그래머스 js 로 풀기
function solution(numbers) {
    var answer = '';
    // 문자로 바꾸고, 문자가 되었을 때 더 큰 순으로 정렬. ex) 3,30일때 '330 vs 303'. 마지막으로 합치기.
    answer = numbers.map(c => String(c)).sort((a,b) => (b+a)-(a+b)).join('');
    
    return answer[0] === '0' ? '0':answer
    
}