// Run by Node.js
const readline = require("readline");

const solution = (N, T) => {
  for (let r = 2; r <= 16; r++) {
    let res = N.toString(r);

    res = res.toUpperCase();
    if (res == T) return r; // r진법 변환이 T결과와 같다면 답은 r진법.
  }
};
(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let T;
  for await (const line of rl) {
    const input = line.split(" ");
    N = +input[0];
    T = input[1];
    rl.close();
  }

  const answer = solution(N, T);

  console.log(answer);

  process.exit();
})();
// 구름 Level문제
