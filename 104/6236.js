const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const check = (value) => {
  let cnt = 1;
  let remain = value;
  for (const money of arr) {
    if (money <= remain) {
      remain -= money;
    } else {
      cnt += 1;
      remain = value - money;
    }
  }
  return cnt <= m;
};
const solution = () => {
  let s = Math.max(...arr); // k원만 인출 가능하므로, 최댓값이 최소 범위가 된다.
  let e = 10000 * 100000; // 최대 금액 . N일 * 이용금액 최대. 해당 금액으로 모든 N일 감수할 수 있음.
  let answer = e;
  while (s <= e) {
    const mid = parseInt((s + e) / 2);
    if (check(mid)) {
      answer = mid;
      e = mid - 1;
    } else {
      s = mid + 1;
    }
  }
  console.log(answer);
};

let [n, m] = [null, null];
let arr = [];
let total = 0;
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    arr.push(+line);
    total += 1;
    if (total === n) {
      rl.close();
    }
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 용돈 관리.
