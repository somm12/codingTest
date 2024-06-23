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
const dfs = (x, y, tmp) => {
  tmp[x][y] = 2;
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i], y + dy[i]];
    if (inRange(nx, ny) && tmp[nx][ny] == 0) dfs(nx, ny, tmp);
  }
};
const spread = (tmp) => {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (tmp[x][y] == 2) dfs(x, y, tmp); //바이러스는 주변 인접한 곳으로 퍼진다.
    }
  }
};
const area = (tmp) => {
  let total = 0;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (tmp[x][y] == 0) total += 1;
    }
  }
  return total;
};
const choose = (L, g) => {
  if (L == 3) {
    // 벽 3개 고르기.
    let tmp = [];
    for (const ar of g) tmp.push([...ar]); // 복사하기.
    spread(tmp); //바이러스 확산.
    answer = Math.max(answer, area(tmp)); // 확산 후 안전 지역 세기.
    return;
  }
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (g[x][y] == 0) {
        g[x][y] = 1;
        choose(L + 1, g);
        g[x][y] = 0;
      }
    }
  }
};
const solution = () => {
  choose(0, g);
  console.log(answer);
};
let answer = 0;
let [n, m] = [null, null];
let g = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) [n, m] = line.split(" ").map((e) => +e);
  else {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 연구소.
