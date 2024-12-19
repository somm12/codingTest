const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const dp = new Array(k + 1).fill(Infinity);
  dp[0] = 0;
  for (let i = 0; i < n; i++) {
    const value = arr[i];
    for (let j = value; j <= k; j++) {
      // 해당 동전의 가치부터 목표 가치 까지 최소 필요한 개수 갱신하기. 현재 동전의 가치를 빼서 +1 씩 개수 증가
      dp[j] = Math.min(dp[j], dp[j - value] + 1);
    }
  }
  if (dp[k] === Infinity) console.log(-1);
  else console.log(dp[k]);
};
let cnt = 0;
const arr = [];
let [n, k] = [null, null];

rl.on("line", (line) => {
  if (!n) {
    [n, k] = line.split(" ").map((e) => +e);
  } else {
    arr.push(+line);
    cnt += 1;
    if (cnt === n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 동전 2. 복습하기.
