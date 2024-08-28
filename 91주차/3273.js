const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,

  output: process.stdout,
});
const solution = () => {
  // 투 포인터 기법 사용.
  let answer = 0;
  arr.sort((a, b) => a - b); // 순서대로 정렬. 포인터 이동시, 값이 오른쪽으로 갈 수 록 커지도록 만듦.
  let [s, e] = [0, n - 1];
  while (s < e) {
    // 서로 다른 두 수의 합 쌍이 x가 되는 수.
    const v = arr[s] + arr[e];
    if (v >= x) {
      // 값이 더 크거나 같다면, 끝에 포인터를 -1.
      if (v == x) answer += 1;
      e -= 1;
    } else {
      // 값이 작다면, 시작 포인터를 +1
      s += 1;
    }
  }
  console.log(answer);
};
let n = null;
let arr = null;
let x = null;

rl.on("line", (line) => {
  if (!n) n = +line;
  else if (!arr) arr = line.split(" ").map((e) => +e);
  else {
    x = +line;
    rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 두 수의 합.
