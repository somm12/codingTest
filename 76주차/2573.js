const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const melting = () => {
  const tmp = g.map((ar) => [...ar]);
  for (let x = 1; x < N - 1; x++) {
    for (let y = 1; y < M - 1; y++) {
      if (g[x][y] > 0) {
        let cnt = 0;
        for (let i = 0; i < 4; i++) {
          const [nx, ny] = [x + dx[i], y + dy[i]];
          if (g[nx][ny] == 0) cnt += 1;
        }
        tmp[x][y] -= cnt;
        if (tmp[x][y] < 0) tmp[x][y] = 0;
      }
    }
  }

  g = tmp.map((ar) => [...ar]);
};

const dfs = (x, y) => {
  visited[x][y] = 1;
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (!visited[nx][ny] && g[nx][ny] > 0) {
      dfs(nx, ny);
    }
  }
};

const cnt = () => {
  let cnt = 0;
  for (let x = 1; x < N - 1; x++) {
    for (let y = 1; y < M - 1; y++) {
      if (g[x][y] > 0 && !visited[x][y]) {
        dfs(x, y);
        cnt += 1;
      }
    }
  }
  visited = Array(N)
    .fill()
    .map((e) => Array(M).fill(0));
  return cnt;
};
const solution = () => {
  let isExit = false;
  let year = 0;
  while (true) {
    melting();

    year += 1;
    const total = cnt();

    if (total >= 2) {
      isExit = true;
      console.log(year);
      break;
    } else if (total == 0) break;
  }
  if (!isExit) console.log(0);
};

let [N, M] = [null, null];
let g = [];
let l = 0;
let visited = [];
rl.on("line", (line) => {
  if (!N) {
    [N, M] = line.split(" ").map((e) => +e);
    visited = Array(N)
      .fill()
      .map((e) => Array(M).fill(0));
  } else {
    g.push(line.split(" ").map((e) => +e));
    l += 1;
    if (l == N) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
