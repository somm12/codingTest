const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const dp = new Array(n).fill().map((e) => Array(1 << n).fill(-1)); // 비트 바스킹으로 방문 처리를 표현하기

  const tsp = (here, visited) => {
    console.log(here, visited);
    if (visited === (1 << n) - 1) {
      // 모두 방문한 경우.
      return dist[here][0] ? dist[here][0] : Infinity;
    }
    let ret = dp[here][visited];
    if (ret !== -1) return dp[here][visited]; // 이미 값이 있다면 반환.
    dp[here][visited] = Infinity;
    for (let i = 0; i < n; i++) {
      if (visited & (1 << i)) continue;
      if (dist[here][i] === 0) continue;
      dp[here][visited] = Math.min(dp[here][visited], tsp(i, visited | (1 << i)) + dist[here][i]); // 재귀로 i까지 오는데 걸리는 최소 비용 저장.
    }
    return dp[here][visited];
  };
  console.log(tsp(0, 1));
};
const dist = [];
let n = null;
let cnt = 0;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    dist.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt === n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 외판원 순회.
