const solution = () => {
  let answer = [];
  let arr = ["A", "B", "C", "D", "E", "F"];
  data.forEach((s) => {
    let tmp = []; //구성
    let prev = "";
    for (let v of s) {
      if (prev !== v) {
        tmp.push(v);
        prev = v;
      }
    }
    let flag = false;
    for (let v of tmp) {
      if (!arr.includes(v)) {
        flag = true;
        answer.push("Good");
        break;
      }
    }
    if (!flag) {
      let [a, f, c] = [tmp.indexOf("A"), tmp.indexOf("F"), tmp.indexOf("C")];
      if (a + 1 === f && f + 1 === c) answer.push("Infected!");
      else answer.push("Good");
    }
  });
  answer = answer.join("\n");
  console.log(answer);
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
    data.push(line);
    count += 1;
  }
  if (count === N) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 자료구조 문제
