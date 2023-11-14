const solution = (data) => {
  data.forEach((v) => {
    let cnt = 0;
    let isDone = false;
    for (let s of v) {
      if (s === ")") {
        cnt -= 1;
        if (cnt < 0) {
          isDone = true;
          console.log("NO");
          break;
        }
      } else {
        cnt += 1;
      }
    }

    if (!isDone) {
      if (cnt === 0) {
        console.log("YES");
      } else console.log("NO");
    }
  });
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let tc = null;
let count = 0;
let data = [];
rl.on("line", (line) => {
  if (!tc) {
    tc = +line;
  } else {
    data.push(line);
    count += 1;
  }
  if (count === tc) {
    rl.close();
  }
}).on("close", () => {
  solution(data);
  process.exit();
});
// 백준 문제. 우선순위가 높은것 먼저.처리
