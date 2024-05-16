const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inRange = (x, y) => {
  // 범위 벗어나는지 체크.
  return 0 <= x && x < n && 0 <= y && y < m;
};

const solution = () => {
  const tmp = g.map((r) => [...r]); //복사
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      let cnt = 0;
      if (g[x][y] == "X") {
        for (let i = 0; i < 4; i++) {
          const [nx, ny] = [x + dx[i], y + dy[i]];
          if (!inRange(nx, ny) || g[nx][ny] == ".") cnt += 1; // 벗어나거나 바다면 카운팅.
        }
      }
      if (cnt >= 3) {
        //3개 이상 바다가 인접한다면 바다로 변한다.(잠김.)
        tmp[x][y] = ".";
      }
    }
  }

  let [x1, x2, y1, y2] = [0, 0, 10, 0]; // 출력하는 범위 구하기. 시작 끝 행과 열 찾기.
  for (let x = 0; x < n; x++) {
    if (tmp[x].includes("X")) {
      // 땅이 처음 등장하는 행.
      x1 = x;
      break;
    }
  }

  for (let x = n - 1; x >= 0; x--) {
    // 땅이 마지막으로 등장하는 행.
    if (tmp[x].includes("X")) {
      x2 = x;
      break;
    }
  }
  for (let x = x1; x < x2 + 1; x++) {
    // 땅이 처음으로 등장하는 열.
    for (let y = 0; y < m; y++)
      if (tmp[x][y] == "X") {
        y1 = Math.min(y1, y);
        y2 = Math.max(y2, y);
      }
  }

  for (let x = x1; x < x2 + 1; x++) {
    // 땅이 마지막으로 등장하는 열.
    let s = "";
    for (let y = y1; y < y2 + 1; y++) {
      s += tmp[x][y];
    }
    console.log(s);
  }
};
const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];
let n = null;
let m = null;
let g = [];
let row = 0;
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    g.push(line.split(""));
    row += 1;
    if (row == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
