const solution = () => {
  let set = new Set();
  let visit = Array(n).fill(0);

  const dfs = (res, L) => {
    if (L === k) {
      set.add(res);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (!visit[i]) {
        visit[i] = 1;
        dfs(res + data[i], L + 1);
        visit[i] = 0;
      }
    }
  };
  dfs("", 0);

  console.log(set.size);
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = null;
let k = null;
let data = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else if (!k) {
    k = +line;
  } else {
    data.push(+line);
    cnt += 1;
  }
  if (cnt === n) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 문제
