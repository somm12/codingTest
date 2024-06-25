const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dfs = (start) => {
  // while문 사용.
  const stack = [start];
  visited = new Array(n + 1).fill(0);
  visited[start] = 1;
  let count = 0;
  while (stack.length) {
    const node = stack.pop();
    for (let v of g[node]) {
      if (visited[v]) continue;
      visited[v] = 1;
      stack.push(v);
      count++;
    }
  }
  return count;
};

const solution = () => {
  const dist = Array(n + 1).fill(0);
  let maxV = 0;
  for (let i = 1; i < n + 1; i++) {
    visited = Array(n + 1).fill(0);
    dist[i] = dfs(i); // 몇 개까지 깊이 들어갈 수 있는가.
    maxV = Math.max(maxV, dist[i]); // 최댓값 업데이트.
  }
  const answer = [];
  for (let i = 1; i < n + 1; i++) {
    if (dist[i] == maxV) answer.push(i); //해당 노드가 최댓값이라면 정답 배열에 추가.
  }

  answer.sort((a, b) => a - b);
  console.log(answer.join(" "));
};
let [n, m] = [null, null];
let cnt = 0;
let g;
let visited;

rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
    g = Array(n + 1)
      .fill()
      .map((e) => Array());
    visited = Array(n + 1).fill(0);
  } else {
    const [a, b] = line.split(" ").map((e) => +e);
    g[b].push(a);
    cnt += 1;
    if (cnt == m) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 효율적인 해킹
