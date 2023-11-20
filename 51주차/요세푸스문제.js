const solution = () => {
  let answer = [];
  let arr = [];
  for (let i = 1; i <= N; i++) arr.push(i);
  let idx = K - 1;
  let data = arr[idx];

  while (arr.length) {
    answer.push(arr[idx]);
    arr = arr.filter((v, i) => i !== idx);
    idx = (idx + K - 1) % arr.length;
  }
  const tmp = answer.join(", ");
  console.log(`<${tmp}>`);
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let [N, K] = [null, null];

rl.on("line", (line) => {
  if (!N) {
    [N, K] = line.split(" ").map((e) => +e);
  }
  rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 자료구조 문제
