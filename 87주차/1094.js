const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = 0;
  for (let j = 0; j <= 6; j++) {
    // 각 j번째 비트가 켜져있다면 +1
    if (x & (1 << j)) answer += 1;
  }
  console.log(answer);
};

let x = null;

rl.on("line", (line) => {
  if (!x) {
    x = +line;
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 막대기.
