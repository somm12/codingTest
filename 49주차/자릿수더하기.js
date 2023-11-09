function solution(n) {
  var answer = 0;
  let a = String(n);
  for (let v of a) {
    answer += Number(v);
  }
  return answer;
}
