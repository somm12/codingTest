function solution(n, numlist) {
  var answer = [];
  answer = numlist.filter((v) => v % n === 0);
  return answer;
}
// n으로 나누어 떨어지지 않는 수 다 제거.
// filter 함수 이용해서 나누어 떨어지는 부분만 반환.
// 프로그래머스
