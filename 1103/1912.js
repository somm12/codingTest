const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const dp = new Array(n).fill(-1001); // 가장 최소가 되는 값은 -1001이므로 이를 할당 해준다.
  dp[0] = arr[0];
  for (let i = 1; i < n; i++) {
    dp[i] = Math.max(dp[i], dp[i - 1] + arr[i]);
  }
  console.log(Math.max(...dp));
};
let n = null;
let arr = null;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
//백준 연속합 문제
