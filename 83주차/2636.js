const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const inRange = (x, y) => {
  return 0 <= x && x < n && 0 <= y && y < m;
};

const check = () => {
  let total = 0;
  for (const [x, y] of arr) g[x][y] = 0;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      total += g[x][y];
    }
  }
  return total;
};
const dfs = (x, y) => {
  visited[x][y] = 1;
  if (g[x][y] == 1) {
    //1을 만나면 재귀 멈추기.
    arr.push([x, y]);
    return;
  }
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (inRange(nx, ny) && visited[nx][ny] == 0) {
      dfs(nx, ny);
    }
  }
};
const solution = () => {
  let t = 0;
  let answer = 0;
  while (true) {
    const total = check();
    if (total == 0) break;
    else {
      answer = total;
    }
    arr = [];
    visited = Array(n)
      .fill()
      .map((e) => Array(m).fill(0));

    dfs(0, 0);
    t += 1;
  }
  console.log(t);
  console.log(answer);
};

let [n, m] = [null, null];
let g = [];
let cnt = 0;
let arr = []; //현재 턴에서 사라지는 치즈 좌표를 담을 배열.
let visited;
rl.on("line", (line) => {
  if (!n) [n, m] = line.split(" ").map((e) => +e);
  else {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  visited = Array(n)
    .fill()
    .map((e) => Array(m).fill(0));
  solution();
  process.exit();
});
// 백준 치즈.
