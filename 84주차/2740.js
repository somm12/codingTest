const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const answer = Array(n)
    .fill()
    .map(() => Array(k).fill(0));
  for (let i = 0; i < n; i++) {
    const arr1 = A[i];

    for (let y = 0; y < k; y++) {
      const arr2 = [];
      let total = 0;
      for (let x = 0; x < m; x++) arr2.push(B[x][y]); // 짝이 되는 배열 구하기.
      for (let idx = 0; idx < arr1.length; idx++) {
        // 배열 끼리 곱한 것 더하기.
        total += arr1[idx] * arr2[idx];
      }
      answer[i][y] = total; // n*k 배열이 최종 크기이므로, i번째 행,y번째 열에 값을 할당.
    }
  }
  for (let i = 0; i < n; i++) {
    console.log(answer[i].join(" "));
  }
};
let [n, m] = [null, null];
let A = [];
let k = null;
let B = [];
let cnt1 = 0;
let cnt2 = 0;
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else if (cnt1 < n) {
    A.push(line.split(" ").map((e) => +e));
    cnt1 += 1;
  } else if (!k) {
    [m, k] = line.split(" ").map((e) => +e);
  } else {
    B.push(line.split(" ").map((e) => +e));
    cnt2 += 1;
    if (cnt2 == m) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 행렬 곱셈.
