const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  arr.sort((a, b) => a[0] - b[0]);
  let idx = 0; // 최근까지 골판지의 위치 표시
  let answer = 0;

  for (const [s, e] of arr) {
    if (e <= idx) continue; //골판지 하나가 여러 웅덩이 감싸는 상황.
    if (idx < s) {
      // 다음 골판지가 끝에서 떨어진 모양.
      cnt = parseInt((e - s) / L);
      cnt += (e - s) % L ? 1 : 0;
      idx = s + L * cnt;
    } else {
      // 다음 골판지가 이전골판지와 겹치는 모양.
      cnt = parseInt((e - idx) / L);
      cnt += (e - idx) % L ? 1 : 0;
      idx = idx + L * cnt;
    }

    answer += cnt;
  }
  console.log(answer);
};
let n = null;
let L = null;
const arr = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) [n, L] = line.split(" ").map((e) => +e);
  else if (cnt < n) {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
});
// 백준 흙기 보수하기
