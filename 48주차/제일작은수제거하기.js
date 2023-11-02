function solution(arr) {
  var answer = [];
  const minV = Math.min(...arr);
  answer = arr.filter((v) => v !== minV);
  return answer.length === 0 ? [-1] : answer;
}
// filter 사용해서 해당하는 수 제외해서 반환.
