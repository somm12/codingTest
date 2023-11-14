const solution = (s) => {
  const n = s.length;
  const set = new Set();
  for (let i = 1; i <= n; i++) {
    // 길이
    for (let j = 0; j < n; j++) {
      if (j + i <= n) {
        let tmp = s.slice(j, j + i);
        set.add(tmp);
      }
    }
  }
  console.log(set.size);
  return;
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
  solution(data);
  process.exit();
});
