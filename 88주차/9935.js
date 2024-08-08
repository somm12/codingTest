const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  ouput: process.stdout,
});
const solution = () => {
  let stk = [];

  for (let i = 0; i < s.length; i++) {
    stk.push(s[i]);
    if (stk.length < target.length) continue;
    let tmp = "";
    for (let j = stk.length - target.length; j < stk.length; j++) {
      tmp += stk[j];
    }
    if (tmp == target) {
      for (let j = 0; j < target.length; j++) stk.pop();
    }
  }
  if (stk.length === 0) console.log("FRULA");
  else console.log(stk.join(""));
};

let s = null;
let target = null;

rl.on("line", (line) => {
  if (!s) s = line;
  else {
    target = line;
    rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 문자열 폭발.
