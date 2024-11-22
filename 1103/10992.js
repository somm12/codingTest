const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const cnt = 2 * n - 1;

  const star = new Array(n).fill().map((e, idx) => new Array(idx + n).fill(" "));
  const mid = parseInt((n * 2 - 1) / 2);

  for (let i = 1; i <= n - 2; i++) {
    star[i][mid - i] = "*";
    star[i][n * 2 - 2 - (mid - i)] = "*";
  }
  star[n - 1] = new Array(cnt).fill("*");
  star.forEach((arr) => console.log(arr.join("")));
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
// 별찍기 17
