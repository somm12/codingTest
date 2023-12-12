const solution = () => {
  let tmp = [1, 1, 1, 1, 1, 1];
  let arr = [];
  let a = 4;
  let total = 4;
  let cycle = 1;
  while (total < T) {
    cycle += 1;
    a += 1;
    total += a;
  }
  for (let i = 0; i < cycle; i++) {
    // T번째 번데기/뻔이 되기까지 필요한 cycle 수만큼 n회차 반복.
    for (let i = 0; i < 6; i++) {
      if (i % 2 === 0) {
        // 뻔
        if (i < 4) arr.push(0);
        else {
          // 끝에 두 부분은 n+1만큼 반복
          tmp[i] += 1;
          for (let j = 0; j < tmp[i]; j++) arr.push(0);
        }
      } else {
        // 데기
        if (i < 5) arr.push(1);
        else {
          tmp[i] += 1;
          for (let j = 0; j < tmp[i]; j++) arr.push(1);
        }
      }
    }
  }

  let answer;
  let [cnt0, cnt1, cnt] = [0, 0, 0];
  for (let v of arr) {
    if (v === 0) cnt0 += 1;
    else cnt1 += 1;
    cnt += 1;
    if ((target === 0 && cnt0 === T) || (target === 1 && cnt1 === T)) {
      answer = cnt % A === 0 ? A - 1 : (cnt % A) - 1; // 마지막이라면 A-1번째. 아니면 번째수 % A -1(0부터 시작이므로)
      break;
    }
  }
  console.log(answer);
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let A = null;
let T = null;
let target = null;

rl.on("line", (line) => {
  if (!A) {
    A = +line;
  } else if (!T) {
    T = +line;
  } else {
    target = +line;
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 문제
