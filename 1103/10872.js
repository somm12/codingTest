const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  const fac = (num) => {
    if (num === 0) return 1;
    return num * fac(num - 1);
  };
  console.log(fac(n));
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
// 백준 피보나치. 재귀.
