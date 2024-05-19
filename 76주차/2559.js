const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  let total = 0;
  let answer = -100 * n;
  for (let i = 0; i < k; i++) {
    // 먼저 k개 연속되는 수들의 합을 구하기.
    total += arr[i];
  }
  answer = Math.max(answer, total);
  for (let i = k; i < n; i++) {
    // 하나씩 더하고, k만큼 뒤떨어진 값은 빼주는 방식 : 슬라이딩 윈도우.
    total += arr[i];
    total -= arr[i - k];
    answer = Math.max(answer, total);
  }
  console.log(answer);
};

let n = null;
let k = null;
let arr = [];
rl.on("line", (line) => {
  if (!n) {
    [n, k] = line.split(" ").map((e) => +e);
  } else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});

// 또 다른 풀이.

const solution = () => {
  let total = 0;
  let answer = -100 * n;
  let psum = Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    // 먼저 k개 연속되는 수들의 합을 구하기.
    total += arr[i - 1];
    psum[i] = total;
  }
  console.log(psum);

  for (let i = k; i <= n; i++) {
    // 하나씩 더하고, k만큼 뒤떨어진 값은 빼주는 방식 : 슬라이딩 윈도우.

    answer = Math.max(answer, psum[i] - psum[i - k]);
  }
  console.log(answer);
};
