const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = 0;
  const prime = Array(n + 1).fill(1); // n까지 소수인지 여부 나타냄.
  for (let i = 2; i <= n; i++) {
    if (prime[i] == 0) continue;
    let j = 2;
    while (i * j <= n) {
      prime[i * j] = 0; //소수가 아니다.
      j += 1;
    }
  }

  const arr = []; // 순서대로 소수 값 push.
  for (let i = 2; i < n + 1; i++) {
    if (prime[i] == 1) arr.push(i);
  }
  let e = 0;
  let total = 0;
  // 연속 합이 n이 되는 순간 세기. 투포인터.
  for (let start = 0; start < arr.length; start++) {
    while (e < arr.length && total < n) {
      total += arr[e];
      e += 1;
    }
    if (total == n) answer += 1;
    total -= arr[start];
  }
  console.log(answer);
};

let n = null;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 소수의 연속 합.
