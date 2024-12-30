const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const dp = new Array(n).fill().map((e) => new Array(1 << n).fill(-1));
  // 현재 위치와 방문 여부를 비트 마스킹으로 표현하기.
  // 1,2 => 3 이든 2,1 => 3 이든 같음. 최소 비용을 계산하기에 순서는 상관없이 현재 위치와 방문 여부로 표현가능하다.
  // 출발지점이 어디든 총 비용은 같기에 0번에서 출발.(인덱스 이용하기 위해서 0번이 출발지점)
  const tsp = (here, visited) => {
    if (visited === (1 << n) - 1) {
      // 모두 다 방문했다면, 출발지점 0으로 돌아가기.
      return dist[here][0] ? dist[here][0] : Infinity;
    }
    if (dp[here][visited] !== -1) {
      return dp[here][visited];
    }
    dp[here][visited] = Infinity; // dp값이 없으므로, 최소비용을 계산해야하기에 infinity를 채운다.

    for (let i = 0; i < n; i++) {
      if (visited & (1 << i)) continue;
      if (dist[here][i] === 0) continue;
      dp[here][visited] = Math.min(dp[here][visited], tsp(i, visited | (1 << i)) + dist[here][i]);
    }
    return dp[here][visited];
  };
  console.log(tsp(0, 1));
};
let cnt = 0;
const dist = [];
let n = null;

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
// 백준 외판원순회 복습
