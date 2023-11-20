const solution = () => {
  let answer = [];
  let now = 1; // now+1은 다음에 넣을 숫자.

  let stack = [];

  for (let i = 0; i < N; i++) {
    const number = data[i];
    while (now <= number) {
      stack.push(now);
      now += 1;
      answer.push("+");
    }
    const top = stack.pop();
    if (top !== number) {
      console.log("NO");
      return;
    }
    answer.push("-");
  }
  console.log(answer.join("\n"));
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N = null;
let data = [];
let count = 0;
rl.on("line", (line) => {
  if (!N) {
    N = +line;
  } else {
    data.push(+line);
    count += 1;
  }
  if (count === N) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 자료구조 문제
