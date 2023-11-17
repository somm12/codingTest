const dx = [0, -1, -1, -1, 0, 1, 1, 1];
const dy = [-1, -1, 0, 1, 1, 1, 0, -1];
let cloud = [];
const move = (d, s) => {
  let newCloud = [];
  cloud.forEach(([x, y]) => {
    let nx = (x + dx[d] * s) % N;
    let ny = (y + dy[d] * s) % N;
    nx = nx >= 0 ? nx : nx + N;
    ny = ny >= 0 ? ny : ny + N;
    newCloud.push([nx, ny]);
  });
  cloud = newCloud;
};
const rain = () => {
  cloud.forEach(([x, y]) => {
    g[x][y] += 1;
  });
};
const remove = () => {
  let except = [...cloud];
  cloud = [];
  return except;
};
const inRange = (nx, ny) => {
  return 0 <= nx && nx < N && 0 <= ny && ny < N;
};
const magic = (block) => {
  block.forEach(([x, y]) => {
    [1, 3, 5, 7].forEach((v) => {
      let [nx, ny] = [x + dx[v], y + dy[v]];
      if (inRange(nx, ny) && g[nx][ny] > 0) g[x][y] += 1;
    });
  });
};
const makeCloud = (except) => {
  const dict = {};
  except.forEach(([x, y]) => {
    dict[[x, y]] = 1;
  });
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (g[i][j] >= 2 && !([i, j] in dict)) {
        cloud.push([i, j]);
        g[i][j] -= 2;
      }
    }
  }
};
const solution = () => {
  cloud = [
    [N - 1, 0],
    [N - 1, 1],
    [N - 2, 0],
    [N - 2, 1],
  ];
  for (let [d, s] of command) {
    d -= 1;
    move(d, s);
    rain();
    let except = remove();
    magic(except);
    makeCloud(except);
  }
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      answer += g[i][j];
    }
  }
  console.log(answer);
  return;
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let answer = 0;
let N = null;
let M = null;
let [nCnt, mCnt] = [0, 0];
let command = [];
let g = [];

rl.on("line", (line) => {
  if (!N) {
    [N, M] = line.split(" ").map((e) => +e);
  } else if (nCnt < N) {
    g.push(line.split(" ").map((e) => +e));
    nCnt += 1;
  } else if (mCnt < M) {
    command.push(line.split(" ").map((e) => +e));
    mCnt += 1;
  }
  if (nCnt >= N && mCnt >= M) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
