function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i < parseInt(num ** 0.5) + 1; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
function solution(numbers) {
  var answer = 0;
  var arr = {};
  let visited = new Array(numbers.length).fill(0);
  function dfs(res) {
    if (res.length > 0) if (isPrime(parseInt(res))) arr[parseInt(res)] = 1;

    for (let i = 0; i < numbers.length; i++) {
      if (!visited[i]) {
        visited[i] = 1;
        dfs(res + numbers[i]);
        visited[i] = 0;
      }
    }
  }

  dfs("");

  arr = Object.keys(arr);
  return arr.length;
}
