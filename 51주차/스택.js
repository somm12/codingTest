const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N = null;
let count = 0;
let stack = [];
let answer = [];
rl.on("line", (line) => {
  if (!N) {
    N = +line;
  } else {
    let a;
    const data = line.split(" ");
    if (data.length === 2) {
      stack.push(parseInt(data[1]));
    } else {
      const tmp = data[0]; //명령어
      if (tmp === "pop") {
        a = stack.length > 0 ? stack.pop() : -1;
      }
      if (tmp === "size") a = stack.length;
      if (tmp === "empty") {
        a = stack.length > 0 ? 0 : 1;
      }
      if (tmp === "top") {
        a = stack.length > 0 ? stack[stack.length - 1] : -1;
      }
      answer.push(a);
    }
    count += 1;
  }
  if (count === N) {
    console.log(answer.join("\n"));
    rl.close();
  }
}).on("close", () => {
  process.exit();
});
// 백준 자료구조 문제
// console.log는 느리므로, 답을 모아서 한번에 출력 할 것.
