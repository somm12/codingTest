const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const go = (x) => {
  // dp값이 이미 구해진 상태에서, 경로 차이가 1 인 것을 이용해서 경로를 찾는다.
  if (x === 0) return;
  arr.push(x);
  if (x % 3 === 0 && dp[x] === dp[parseInt(x / 3)] + 1) go(parseInt(x / 3));
  else if (x % 2 === 0 && dp[x] === dp[parseInt(x / 2)] + 1) go(parseInt(x / 2));
  else if (x - 1 >= 0 && dp[x] === dp[x - 1] + 1) go(x - 1);
  return;
};
const arr = [];
const solution = () => {
  dp[1] = 0;
  // dp 값을 먼저 구하기.
  for (let i = 2; i <= n; i++) {
    if (!(i % 3)) {
      dp[i] = Math.min(dp[parseInt(i / 3)] + 1, dp[i]);
    }
    if (!(i % 2)) {
      dp[i] = Math.min(dp[parseInt(i / 2)] + 1, dp[i]);
    }
    dp[i] = Math.min(dp[i - 1] + 1, dp[i]);
  }
  console.log(dp[n]);
  go(n);
  console.log(arr.join(" "));
};
let n = null;
let dp;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    dp = new Array(n + 1).fill(Infinity);
    rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 1로 만들기2
