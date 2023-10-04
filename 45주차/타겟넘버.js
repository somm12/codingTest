function solution(numbers, target) {
  var answer = 0;
  const n = numbers.length;
  function dfs(L, value) {
    if (L === n) {
      if (value === target) answer += 1;
      return;
    }
    dfs(L + 1, value + numbers[L]);
    dfs(L + 1, value - numbers[L]);
  }
  dfs(0, 0);

  return answer;
}
//프로그래머스 dfs 문제
