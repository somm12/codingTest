const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  arr.sort((a, b) => {
    if (a[1] !== b[1]) return a[1] - b[1]; // 빨리 끝나는 회의 기준 정렬.
    return a[0] - b[0]; // 종료시간이 같다면, 시작시간이 빠른 회의를 먼저 해야함. 시작과 끝 시간이 같은 경우 대비.
  });

  let t = 0; // 가장 최근에 끝난 시간
  let answer = 0;
  for (const [st, et] of arr) {
    if (t <= st) {
      answer += 1;
      t = et;
    }
  }
  console.log(answer);
};

let n = null;
const arr = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 회의실 배정
