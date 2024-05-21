const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  let answer = 0;

  for (let s of arr) {
    let stk = [];
    for (let v of s) {
      if (stk.length == 0) stk.push(v);
      else {
        if (v == stk[stk.length - 1]) stk.pop();
        else stk.push(v);
      }
    }
    if (stk.length == 0) answer += 1;
  }

  console.log(answer);
};
let n = null;
let arr = [];
let cnt = 0;

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
// 좋은 단어.
