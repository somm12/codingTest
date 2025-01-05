const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const solution = () => {
  const visited = new Array(n).fill().map(() => new Array(m).fill(0));
  const dp = new Array(n).fill().map(() => new Array(m).fill(0));

  const move = (x, y) => {
    if (x < 0 || x >= n || y < 0 || y >= m || arr[x][y] === "H") {
      return 0;
    }
    if (visited[x][y]) {
      console.log(-1);
      process.exit();
    }
    if (dp[x][y]) {
      return dp[x][y];
    }
    const value = +arr[x][y];
    visited[x][y] = 1;
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i] * value, y + dy[i] * value];
      dp[x][y] = Math.max(dp[x][y], move(nx, ny) + 1);
    }
    visited[x][y] = 0; // 재귀 호출 이후 다시 돌아오면서 방문처리를 지우면서 다른 경우 찾기.
    return dp[x][y];
  };
  console.log(move(0, 0));
};
let cnt = 0;
const arr = [];
let [n, m] = [null, null];

rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    arr.push(line.split(""));
    cnt += 1;
    if (cnt === n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 게임 복습
