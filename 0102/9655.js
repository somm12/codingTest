const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
// 완벽한 게임을 한다고 했을 때 어떻게 고르든 결과는 하나만 나온다는 뜻.
// 3개 또는 1개를 고르므로, 3개 1개 씩 고른다고 했을 때. 상근 부터 시작하기 때문에 4로 나누어서 남은 돌의 개수를 본다.
// 홀수개가 남으면 상근이 이김.
const solution = () => {
  if ((n % 4) % 2 === 1) {
    console.log("SK");
  } else {
    console.log("CY");
  }
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
// 백준 돌게임.
