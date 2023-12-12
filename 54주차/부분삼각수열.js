const solution = () => {
  arr.sort((a, b) => a - b);
  let answer = 0;
  if (arr.length <= 2) console.log(arr.length);
  else {
    for (let i = 0; i < n - 1; i++) {
      for (let j = n - 1; j >= 0; j--) {
        if (arr[i] + arr[i + 1] > arr[j]) {
          answer = Math.max(answer, j - i + 1);
        }
      }
    }
    console.log(answer);
  }
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = null;
let arr = [];
let count = 0;

rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 문제
// x>y>z이고 x+y>z를 만족하면 삼각관계에 해당함.
// 범위를 늘려가며, 가장 큰 수 부터 검사해서 최댓값 구하기.
