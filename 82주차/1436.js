const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const check = (num) => {
  let tmp = num.toString();
  let cnt = 0;
  for (const s of tmp) {
    if (s == "6") {
      cnt += 1;
      if (cnt >= 3) return true;
    } else cnt = 0;
  }
  return false;
};

const solution = () => {
  const arr = [];
  let cnt = 666;
  while (arr.length < n) {
    // n번째 찾을 때 까지 반복.
    if (check(cnt)) arr.push(cnt);
    cnt += 1;
  }
  console.log(arr[n - 1]); // 인덱스는 0부터 시작이므로 N-1번째 출력.
};
let n = null;

rl.on("line", (line) => {
  if (!n) n = +line;
  rl.close();
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 영화감독 숌.
