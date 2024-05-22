const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];
const bfs = (x, y) => {
  visited[x][y] = 1;
  const q = [];
  q.push([x, y]);
  while (q.length > 0) {
    const [x, y] = q.shift();

    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (!visited[nx][ny] && g[nx][ny] == 1) {
          visited[nx][ny] = 1;
          q.push([nx, ny]);
        }
      }
    }
  }
};

const solution = () => {
  let answer = 0;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (!visited[x][y] && g[x][y] == 1) {
        bfs(x, y);
        answer += 1;
      }
    }
  }
  return answer;
};
let [m, n, k] = [null, null, null];
let tc = null;
let visited = [];
let g = [];
let tcCnt = 0;
let cnt = 0;
rl.on("line", (line) => {
  if (!tc) {
    tc = +line;
  } else if (!n) {
    [m, n, k] = line.split(" ").map((e) => +e);
    g = Array(n)
      .fill()
      .map((e) => Array(m).fill(0));
    visited = Array(n)
      .fill()
      .map((e) => Array(m).fill(0));
  } else if (cnt < k) {
    const [y, x] = line.split(" ").map((e) => +e); // 가로 세로 위치 순으로 입력 받음. 주의
    g[x][y] = 1;
    cnt += 1;

    if (cnt == k) {
      console.log(solution());
      [m, n, k] = [null, null, null];
      cnt = 0;
      tcCnt += 1;
      if (tc == tcCnt) rl.close();
    }
  }
});
rl.on("close", () => {
  process.exit();
});
