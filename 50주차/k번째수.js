function solution(array, commands) {
  var answer = [];
  commands.forEach(([i, j, k]) => {
    const tmp = array.slice(i - 1, j);
    tmp.sort((a, b) => a - b);
    answer.push(tmp[k - 1]);
  });

  return answer;
}
// js로 풀기. 정렬 문제.
