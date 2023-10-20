function solution(numbers, target) {
  let answer = 0;
  const n = numbers.length;
  function dfs(L, total) {
    if (L > n) return;
    if (L === n && total === target) {
      // n개 모두 계산했을때, target과 같다면 +1.
      answer += 1;
      return;
    }
    dfs(L + 1, total + numbers[L]); // 덧셈 혹은 뺄셈.
    dfs(L + 1, total - numbers[L]);
  }
  dfs(0, 0);
  return answer;
}
// 프로그래머스 dfs.
