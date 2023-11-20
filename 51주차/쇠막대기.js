const solution = () => {
  let s = [];
  let answer = 0;
  data = [...data];
  data.forEach((v, i) => {
    if (v === "(") s.push(v);
    else {
      s.pop();
      if (data[i - 1] === "(") {
        answer += s.length;
      } else {
        answer += 1;
      }
    }
  });
  console.log(answer);
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = null;
rl.on("line", (line) => {
  if (!data) {
    data = line;
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit;
});
// 백준 자료구조 문제.
