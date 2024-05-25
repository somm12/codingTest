const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const makeG = (arr) => {
  // 각 파티 사람들 그래프로 연결하기
  const combi = (start, res) => {
    if (res.length == 2) {
      const [a, b] = res;
      g[a].add(b);
      g[b].add(a);
      return;
    }
    for (let i = start; i < arr.length; i++) {
      combi(i + 1, [...res, arr[i]]);
    }
  };
  combi(0, []);
};
const bfs = (num) => {
  //  아는 사람을 시작으로, bfs로 퍼뜨려서 최종적으로 아는 사람을 모은다.
  visited[num] = 1;
  const q = [];
  q.push(num);
  while (q.length > 0) {
    const x = q.shift();
    known.add(x);
    for (let nxt of g[x]) {
      if (!visited[nxt]) {
        visited[nxt] = 1;
        q.push(nxt);
      }
    }
  }
};
const solution = () => {
  let answer = 0;

  for (let v of known) {
    // 알게 되는 사람 다 모으기.
    if (!visited[v]) bfs(v);
  }

  for (const p of party) {
    // 모르는 사람만 있는 파티개수세기.
    let flag = true;
    for (const num of p) {
      if (known.has(num)) flag = false;
    }
    if (flag) answer += 1;
  }
  console.log(answer);
};
let [n, m] = [null, null];
let known = null;
let party = [];
let cnt = 0;
let g = [];
let visited;
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
    g = Array(n + 1)
      .fill()
      .map((e) => new Set());
    visited = Array(n + 1).fill(0);
  } else if (!known) {
    known = line.split(" ").map((e) => +e);
    known = known.slice(1);
    known = new Set([...known]);
  } else {
    let tmp = line.split(" ").map((e) => +e);
    tmp = tmp.slice(1);
    party.push(tmp);
    if (tmp.length > 1) makeG(tmp);
    cnt += 1;
    if (cnt == m) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
