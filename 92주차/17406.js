const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

const rotate = (sx, sy, ex, ey, tmp) => {
  const chg = tmp.map((v) => [...v]);

  while (sy < ey) {
    let [x, y] = [sx, sy];
    let d = 0;
    while (true) {
      // 한 테두리 씩 이동.
      let [nx, ny] = [x + dx[d], y + dy[d]];
      if (sx <= nx && nx <= ex && sy <= ny && ny <= ey) {
        chg[nx][ny] = tmp[x][y];
      } else {
        d = (d + 1) % 4; // 시계방향
        nx = x + dx[d];
        ny = y + dy[d];
        chg[nx][ny] = tmp[x][y];
      }
      x = nx;
      y = ny;
      if (nx == sx && ny == sy) {
        break;
      }
    }
    sx += 1;
    sy += 1;
    ex -= 1;
    ey -= 1;
  }
  return chg;
};
const solution = () => {
  const calc = [];
  const visited = Array(k).fill(0);
  let answer = Infinity;
  const dfs = (res) => {
    if (res.length == k) {
      calc.push(res.map((v) => [...v]));

      return;
    }
    for (let i = 0; i < k; i++) {
      if (!visited[i]) {
        visited[i] = 1;
        res.push(arr[i]);
        dfs(res);
        visited[i] = 0;
        res.pop();
      }
    }
  };
  dfs([]); // 순열로 계산순서 뽑기.

  for (const one of calc) {
    let tmp = g.map((v) => [...v]);
    for (const [r, c, s] of one) {
      tmp = rotate(r - s, c - s, r + s, c + s, tmp); // 순서대로 회전시키기.
    }

    let minV = Infinity;
    for (let row of tmp) {
      // 배열 의 값 계산.
      let total = 0;
      for (const v of row) total += v;
      minV = Math.min(minV, total);
    }
    answer = Math.min(answer, minV); // 가장 최솟값 찾기.
  }
  console.log(answer);
};
let [n, m, k] = [null, null, null];
const g = [];
const arr = [];
let cnt2 = 0;
let cnt = 0;
rl.on("line", (line) => {
  if (!n) [n, m, k] = line.split(" ").map((e) => +e);
  else if (cnt < n) {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
  } else {
    const [a, b, c] = line.split(" ").map((e) => +e);
    arr.push([a - 1, b - 1, c]);
    cnt2 += 1;
    if (cnt2 == k) rl.close();
  }
});
rl.on("close", () => {
  solution();
});
// 배열 돌리기4
