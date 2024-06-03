const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = null;
let g = [];
let cnt = 0;
const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];
let visited;
const inRange = (x, y) => 0 <= x && x < n && 0 <= y && y < n;
const dfs = (x, y, h) => {
  visited[x][y] = 1;
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (inRange(nx, ny) && !visited[nx][ny] && g[nx][ny] > h) {
      dfs(nx, ny, h);
    }
  }
};
const solution = () => {
  let answer = 0;
  for (let h = 0; h <= 100; h++) {
    let cnt = 0;
    visited = Array(n)
      .fill()
      .map((e) => Array(n).fill(0));
    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        if (!visited[x][y] && g[x][y] > h) {
          // h이하 부분은 잠긴다고 했을 때,h초과 높이인 부분만 덩어리 세기.
          dfs(x, y, h);
          cnt += 1;
        }
      }
    }
    answer = Math.max(answer, cnt);
  }
  console.log(answer);
};
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    visited = Array(n)
      .fill()
      .map((e) => Array(n).fill(0));
  } else {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 높이가 모두 1일 수도 있기에, 0부터 h를 설정해야 최댓값을 구할 수 있음
// 백준 안전영역.
