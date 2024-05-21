const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  const set = new Set();

  for (const v of arr) {
    set.add(v);
  }
  let cnt = 0;
  for (const v of arr) {
    if (set.has(m - v)) {
      // 두 개의 재료 합이 m이 되는지 확인.
      if (m - v == v) continue;
      // 5 + 5 = 10의 경우 하나의 재료이므로. 아님.
      else cnt += 1; // 같은 쌍이 나오므로 주의!!
    }
  }

  console.log(cnt / 2);
};
let [n, m] = [null, null];
let arr = [];

rl.on("line", (line) => {
  if (!n) n = +line;
  else if (!m) m = +line;
  else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
