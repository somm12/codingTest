const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  for (const s of arr) {
    let tmp = 0;
    for (const v of s) {
      if (v == ")") {
        // 닫는 괄호
        tmp -= 1;
        if (tmp < 0) {
          // 여는 괄호 없이 닫는 괄호 더 많아지면 올바른 괄호가 아님.
          break;
        }
      } else tmp += 1;
    }
    if (tmp == 0) console.log("YES");
    else console.log("NO");
  }
};

let n = null;
let cnt = 0;
let arr = [];
rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(line);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 괄호.
