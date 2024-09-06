const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = 0;
  for (const [a, b, c] of arr) {
    if (a == b && b == c) {
      answer = Math.max(answer, 10000 + a * 1000);
    } else if (a == b || b == c || a == c) {
      if (a == b) answer = Math.max(answer, 1000 + a * 100);
      else if (b == c) answer = Math.max(answer, 1000 + b * 100);
      else if (a == c) answer = Math.max(answer, 1000 + a * 100);
    } else {
      const tmp = Math.max(a, b, c) * 100;
      answer = Math.max(answer, tmp);
    }
  }
  console.log(answer);
};
let n = null;
const arr = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) n = +line;
  else if (cnt < n) {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
});
