const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = 0;

  for (let i = 1; i <= n; i++) {
    if (check(i)) {
      answer += 1;
    }
  }
  console.log(answer);
};
const check = (num) => {
  let diff = 0;
  const s = num.toString();
  for (let i = 0; i < s.length - 1; i++) {
    if (i === 0) {
      diff = +s[i + 1] - s[i];
      continue;
    }
    if (s[i + 1] - s[i] !== diff) return false;
  }
  return true;
};
let n = null;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 한수
