const { loadEnvFile } = require("process");
const readline = require("readline");
const { start } = require("repl");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const go = (start, link) => {
  let [a, b] = [0, 0];
  for (let i = 0; i < n / 2; i++) {
    for (let j = 0; j < n / 2; j++) {
      if (i == j) continue; // i끼리는 능력치0.
      a += g[start[i]][start[j]];
      b += g[link[i]][link[j]];
    }
  }
  return Math.abs(a - b);
};
const solution = () => {
  let answer = Infinity;
  for (let i = 0; i < 1 << n; i++) {
    // 비트 마스킹으로 모든 경우 찾기.
    let cnt = 0;
    for (let j = 0; j < n; j++) {
      // n/2 개수만큼 1이 있다면, 팀을 나누어 능력치 차이 구하기.
      if (i & (1 << j)) cnt += 1;
    }
    if (cnt == n / 2) {
      const start = [];
      const link = [];
      for (let j = 0; j < n; j++) {
        if (i & (1 << j)) start.push(j); // 1이 라면 스타트
        else link.push(j); // 0이라면 만대로 링크팀.
      }
      answer = Math.min(answer, go(start, link)); // 둘 팀의 능력치 차이.
    }
  }
  console.log(answer);
};

let n = null;
const g = [];

let cnt = 0;
rl.on("line", (line) => {
  if (!n) n = +line;
  else if (cnt < n) {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
});
// 백준 스타트와링크
