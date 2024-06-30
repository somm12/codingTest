const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = Infinity; // 치킨 거리 최솟값을 할당하기 위해 할당.

  const h = []; // 집
  const c = []; // 치킨 집
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      if (g[x][y] == 2) c.push([x, y]);
      if (g[x][y] == 1) h.push([x, y]);
    }
  }

  const dfs = (start, ret) => {
    // 치킨 집 M개 고르기,
    if (ret.length == m) {
      let total = 0; //도시 치킨 거리

      for (const [hx, hy] of h) {
        let dist = 1000;
        for (const [cx, cy] of ret) {
          // 고른 치킨집과 집의 치킨 거리 구하기
          dist = Math.min(dist, Math.abs(hx - cx) + Math.abs(hy - cy));
        }
        total += dist; // 각 집의 치킨 거리합인 도시의 치킨 거리
      }
      answer = Math.min(answer, total); // 도시 치킨 거리 최솟값.

      return;
    }
    for (let i = start; i < c.length; i++) {
      ret.push(c[i]);
      dfs(i + 1, ret);
      ret.pop();
    }
  };
  dfs(0, []);
  console.log(answer);
};
let [n, m] = [null, null];
let cnt = 0;
let g = [];

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
// 백준 치킨 배달.
