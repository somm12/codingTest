const solution = (s, t) => {
  let cnt = 0;
  let l = 0;
  let r = 0;
  while (l < s.length && r < t.length) {
    if (s[l] === t[r]) {
      l += 1;
      r += 1;
      cnt += 1;
    } else r += 1;
  }
  if (cnt === s.length) {
    console.log("Yes");
  } else console.log("No");
  return;
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = null;
let arr = [];
rl.on("line", (line) => {
  if (!data) {
    arr.push(line.split(" "));
  }
}).on("close", () => {
  for (let [s, t] of arr) {
    solution(s, t);
  }
  process.exit();
});
// 이 문제는 EOF 입력이 되어야 입력이 종료되는 형태.
// 백준 문자열 문제.
