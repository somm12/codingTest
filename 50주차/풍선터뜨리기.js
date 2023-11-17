const solution = () => {
  let idx = 0;
  let answer = [];
  let index = [];
  for (let i = 1; i <= n; i++) index.push(i);

  let temp = data[0]; //적힌 수
  data = data.slice(1, n);
  index = index.slice(1, n);
  answer.push(1); //1부터 시작

  while (data.length) {
    if (temp < 0) {
      idx = (idx + temp) % data.length;
      idx = idx >= 0 ? idx : idx + data.length;
    } else {
      idx = (idx + temp - 1) % data.length;
    }
    temp = data[idx];
    data = data.filter((v, i) => idx !== i);
    answer.push(index[idx]);
    index = index.filter((v, i) => i !== idx);
  }
  console.log(answer.join(" "));
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let n = null;
let data = [];

rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    data = line.split(" ").map((e) => +e);
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 자료구조 문제 js로 풀기.
