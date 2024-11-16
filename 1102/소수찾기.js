const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i < parseInt(num ** 0.5) + 1; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

function solution(numbers) {
  var answer = {};
  const n = numbers.length;
  const visited = new Array(n).fill(0);

  const dfs = (L, res) => {
    if (L > 0 && isPrime(parseInt(res))) {
      answer[parseInt(res)] = 1;
    }
    if (L === n) return;

    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        visited[i] = 1;
        dfs(L + 1, res + numbers[i]);
        visited[i] = 0;
      }
    }
  };
  dfs(0, "");

  return Object.keys(answer).length;
}
// 프로그래머스
