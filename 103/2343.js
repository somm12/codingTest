const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const check = (size, maxV) => {
  let cnt = 0;
  let sum = 0;
  if (size < maxV) return false; // 가장 큰 강의 길이가 size 보다 크면 아예 불가능. ***
  for (const v of arr) {
    if (sum + v <= size) {
      sum += v;
    } else {
      sum = v;
      cnt += 1;
    }
  }
  cnt += 1;
  return cnt <= m;
};

const solution = () => {
  let answer = Infinity;
  let s = 0;
  let e = Math.max(...arr) * n;
  const maxV = Math.max(...arr);
  while (s <= e) {
    const mid = parseInt((s + e) / 2);

    if (check(mid, maxV)) {
      // 블루레이 m개로 나누어 진다면, 답 업데이트.
      answer = mid;
      e = mid - 1;
    } else {
      // 불가능 하다면 크기를 늘린다.
      s = mid + 1;
    }
  }
  console.log(answer);
};

let [n, m] = [null, null];
let arr = [];
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});

rl.on("close", () => {
  solution();
});
// 백준 기타 레슨
