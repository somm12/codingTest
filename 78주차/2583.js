const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let [n, m, k] = [null, null, null];
let arr = [];
let cnt = 0;
let g;
let visited;
const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];

const bfs = (x, y) => {
  visited[x][y] = 1;
  const q = [];
  q.push([x, y]);
  let cnt = 0;
  while (q.length > 0) {
    const [x, y] = q.shift();
    cnt += 1;
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
  return cnt;
};
const solution = () => {
  let answer = [];
  for (const [x1, y1, x2, y2] of arr) {
    // 직사각형 그리기.
    for (let x = y1; x < y2; x++) {
      for (let y = x1; y < x2; y++) {
        g[x][y] = 0;
      }
    }
  }

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (!visited[x][y] && g[x][y] == 1) {
        // 영역 구하기: 1인 부분 덩어리 개수.
        answer.push(bfs(x, y));
      }
    }
  }
  answer.sort((a, b) => a - b); //오름차순 정렬.
  console.log(answer.length);
  console.log(answer.join(" "));
};
rl.on("line", (line) => {
  if (!n) {
    [n, m, k] = line.split(" ").map((e) => +e);
  } else {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == k) rl.close();
  }
});

rl.on("close", () => {
  g = Array(n)
    .fill()
    .map((e) => Array(m).fill(1));
  visited = Array(n)
    .fill()
    .map((e) => Array(m).fill(0));
  solution();
  process.exit();
});
