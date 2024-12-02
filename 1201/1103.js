const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];
const inRange = (x, y) => {
  return 0 <= x && x < n && 0 <= y && y < m;
};

const go = (x, y) => {
  if (!inRange(x, y) || g[x][y] === "H") {
    // 벗어 나거나 구멍에 도착한다면, 0을 반환. 재귀 종료. 이 0으로 부터 +1 씩 더해서 이동 회수를 계산한다.
    return 0;
  }
  if (visited[x][y]) {
    // 재귀 호출하다가 이미 방문한 위치는 사이클이 생긴 것이므로, -1 출력.
    console.log(-1);
    process.exit();
  }
  if (dp[x][y] !== 0) {
    // 이미 값이 있다면 반환.
    return dp[x][y];
  }
  visited[x][y] = 1; // 방문 처리.
  const value = +g[x][y];
  for (let i = 0; i < 4; i++) {
    const [nx, ny] = [x + dx[i] * value, y + dy[i] * value]; // 해당 칸 만큼, 상하좌우 중 하나로 이동.
    dp[x][y] = Math.max(dp[x][y], go(nx, ny) + 1); // 재귀 호출을 통해 반환되는 값을 저장. 결국 최종적으로 이동 횟수 최댓값이 저장됨.
  }
  visited[x][y] = 0; // 다시 방문 처리. (다른 경우의 수를 계산하기 위해.)
  return dp[x][y];
};
const solution = () => {
  console.log(go(0, 0));
};
let visited;
let dp;
const g = [];
let cnt = 0;
let [n, m] = [null, null];
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    g.push(line.split(""));
    cnt += 1;
    if (cnt === n) rl.close();
  }
});

rl.on("close", () => {
  visited = new Array(n).fill().map((e) => Array(m).fill(0));
  dp = new Array(n).fill().map((e) => Array(m).fill(0));
  solution();
  process.exit();
});
//  백준 게임. 다시 풀어보기
