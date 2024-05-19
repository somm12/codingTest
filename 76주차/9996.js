const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const idx = p.indexOf("*");
  const p1 = p.slice(0, idx);
  const p2 = p.slice(idx + 1);

  for (let s of arr) {
    const s1 = s.slice(0, idx);
    s = s.slice(idx);
    const s2 = s.slice(s.length - p2.length); // aaa*a 와 a 일때 경우를 대비해서 앞부분 자르기.
    if (p1 == s1 && p2 == s2) console.log("DA");
    else console.log("NE");
  }
};
let n = null;
let p = null;
let arr = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else if (!p) p = line;
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
