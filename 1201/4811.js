const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dp = new Array(31).fill().map((e) => Array(31).fill(0));
const go = (W, H) => {
  // W: 한 개 알약. H: 반 개 알약 각 개수.
  if (W === 0 && H === 0) return 1; // 가장 마지막 끝이 되는 부분에서 1을 반환해서 차곡차곡 경우의 수를 더해나간다.
  if (dp[W][H]) return dp[W][H];

  if (W > 0) {
    // 한 개 짜리 알약을 꺼낸다면, 반개는 새로 생기고, 한 개는 개수가 줄어듦.
    dp[W][H] += go(W - 1, H + 1);
  }
  if (H > 0) {
    // 반 개 짜리 알약을 꺼낸다면
    dp[W][H] += go(W, H - 1); // 반 개는 개수만 줄어듦.
  }
  return dp[W][H]; // 합쳐진 경우의 수를 반환.
};

rl.on("line", (line) => {
  if (+line === 0) {
    rl.close();
  } else {
    console.log(go(+line, 0));
  }
});

rl.on("close", () => {
  process.exit();
});
//  백준 알약
