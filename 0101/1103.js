const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const solution = () => {
  const check = new Array(n).fill().map((e) => new Array(m).fill(0));
  const dp = new Array(n).fill().map((e) => new Array(m).fill(0));
  const go = (x, y) => {
    if (x < 0 || x >= n || y < 0 || y >= m || arr[x][y] === "H") return 0;
    if (check[x][y]) {
      console.log(-1);
      process.exit();
    }

    if (dp[x][y]) return dp[x][y];
    check[x][y] = 1; // 방문 처리.

    const value = +arr[x][y];
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i] * value, y + dy[i] * value];
      dp[x][y] = Math.max(dp[x][y], go(nx, ny) + 1); // 한 칸씩 이동.
    }
    check[x][y] = 0; // 해당 지점 방문 처리를 지우고, 다시 다른 지점으로 이동하는 경우를 본다.
    return dp[x][y];
  };

  console.log(go(0, 0)); // 초기 출발점에 최대 몇 번 이동할 수 있는지를 쌓는다.
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
