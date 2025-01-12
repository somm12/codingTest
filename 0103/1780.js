const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const count = [0, 0, 0];
  const recursion = (n, x, y) => {
    // x,y는 왼쪽 위를 기준으로한 지점.
    const num = paper[y][x];
    let numCount = 0;
    for (let i = 0; i < n; i++) {
      // 1번 모두 같은지 체크.
      for (let j = 0; j < n; j++) {
        if (paper[y + j][x + i] === num) numCount++;
        else break;
      }
    }
    if (numCount === n * n) count[num + 1]++;
    else {
      // 1번 경우가 아니면 9분할 하기.
      n /= 3;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          recursion(n, x + i * n, y + j * n);
        }
      }
    }
  };
  recursion(n, 0, 0);
  console.log(count.join("\n"));
};
let n = null;
let cnt = 0;
const paper = [];

rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    paper.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt === n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
//백준 종이의 개수
