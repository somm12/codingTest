const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  // 10의 개수 == 5와 2의 개수 중 최솟값. => 제곱수도 있기 때문에 2,4,8, ,, 나누어서 개수 더한 것이 2의 개수.
  for (const v of arr) {
    let [two, five] = [0, 0];
    for (let i = 2; i <= v; i *= 2) {
      two += parseInt(v / i);
    }
    for (let i = 5; i <= v; i *= 5) {
      five += parseInt(v / i);
    }
    console.log(Math.min(two, five));
  }
};
let n = null;
let arr = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(+line);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 교수가 된 현우
