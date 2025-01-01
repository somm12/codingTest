const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const check = (i, j, d) => {
  if (d === 0 || d === 2) {
    if (arr[i][j] === 0) {
      return true;
    }
  } else {
    if (arr[i - 1][j] === 0 && arr[i][j - 1] === 0 && arr[i][j] === 0) {
      return true;
    }
  }
  return false;
};
const solution = () => {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      arr[i + 1][j + 1] = tmp[i][j];
    }
  }

  const dp = new Array(n + 2).fill().map((e) => new Array(n + 2).fill().map((e) => new Array(3).fill(0)));
  dp[1][2][0] = 1;

  // 0: 가로, 1: 대각선, 2:세로
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (check(i, j + 1, 0)) {
        dp[i][j + 1][0] += dp[i][j][0];
      }
      if (check(i + 1, j + 1, 1)) {
        dp[i + 1][j + 1][1] += dp[i][j][0];
      }

      if (check(i + 1, j, 2)) {
        dp[i + 1][j][2] += dp[i][j][2];
      }
      if (check(i + 1, j + 1, 1)) {
        dp[i + 1][j + 1][1] += dp[i][j][2];
      }

      if (check(i, j + 1, 0)) {
        dp[i][j + 1][0] += dp[i][j][1];
      }
      if (check(i + 1, j, 2)) {
        dp[i + 1][j][2] += dp[i][j][1];
      }
      if (check(i + 1, j + 1, 1)) {
        dp[i + 1][j + 1][1] += dp[i][j][1];
      }
    }
  }
  console.log(dp[n][n][0] + dp[n][n][1] + dp[n][n][2]);
};

let cnt = 0;
let arr = [];
const tmp = [];
let n = null;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    arr = new Array(n + 2).fill(0).map((e) => new Array(n + 2).fill(0));
  } else {
    tmp.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt === n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 파이프 옮기기 복습
