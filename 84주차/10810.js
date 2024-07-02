const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const basket = Array(n).fill(0);
  for (const [i, j, k] of arr) {
    for (let idx = i - 1; idx < j; idx++) {
      basket[idx] = k;
    }
  }
  console.log(basket.join(" "));
};
let [n, m] = [null, null];
let cnt = 0;
let arr = [];

rl.on("line", (line) => {
  if (!n) [n, m] = line.split(" ").map((e) => +e);
  else {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == m) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 공넣기
