const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  ouput: process.stdout,
});
const inRange = (x, y) => {
  return 0 <= x && x < n && 0 <= y && y < n;
};
const solution = () => {
  const dx = [-1, 0, 1, 0];
  const dy = [0, 1, 0, -1];
  const arr = Array(n)
    .fill()
    .map((e) => Array(n).fill(0));
  let cnt = 0;
  let d = 0;
  let [x, y] = [parseInt(n / 2), parseInt(n / 2)];
  let k = 2;
  arr[x][y] = 1;
  let [ax, ay] = [0, 0];
  while (inRange(x, y)) {
    if (d % 2 === 0) {
      cnt += 1;
    }
    for (let i = 0; i < cnt; i++) {
      x += dx[d];
      y += dy[d];
      if (inRange(x, y)) {
        arr[x][y] = k;
        k += 1;
      } else break;
    }
    d = (d + 1) % 4;
  }
  for (let i = 0; i < n; i++) {
    const tmp = arr[i].join(" ");
    for (let j = 0; j < n; j++) {
      if (num === arr[i][j]) [ax, ay] = [i + 1, j + 1];
    }
    console.log(tmp);
  }
  console.log(ax, ay);
};
let n = null;
let num = null;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    num = +line;
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
//백준 달팽이
