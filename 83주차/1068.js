const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const q = [num];
  while (q.length > 0) {
    const x = q.shift();
    parent[x] = -2; //삭제
    for (let i = 0; i < n; i++) {
      if (parent[i] == x) q.push(i); // 삭제되는 노드를 부모로가진 자식도 삭제됨.
    }
  }
  let alive = 0; // 살아남은 노드 개수.
  const p = new Set();
  for (let i = 0; i < n; i++) {
    // 자신을 부모로 두지 않는 노드인가(즉 리프노드) 확인 & 그 노드가 삭제되지 않았다면 확실한 리프노드.
    if (parent[i] !== -2) alive += 1;
    if (parent[i] >= 0) p.add(parent[i]); // 부모인 노드들 .
  }

  console.log(alive - [...p].length); // 남은 노드 중에서, 부모 노드가 아닌 노드 빼기.
};
let n = null;
let parent = null;
let num = null;

rl.on("line", (line) => {
  if (!n) n = +line;
  else if (!parent) parent = line.split(" ").map((e) => +e);
  else {
    num = +line;
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 트리.
