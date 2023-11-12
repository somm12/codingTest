const solution = (A, B) => {
  const answer = [];
  let aIdx = 0;
  let bIdx = 0;
  while (aIdx < A.length && bIdx < B.length) {
    if (A[aIdx] < B[bIdx]) {
      answer.push(A[aIdx]);
      aIdx += 1;
    } else {
      answer.push(B[bIdx]);
      bIdx += 1;
    }
  }

  while (aIdx < A.length) {
    answer.push(A[aIdx]);
    aIdx += 1;
  }

  while (bIdx < B.length) {
    answer.push(B[bIdx]);
    bIdx += 1;
  }
  console.log(answer.join(" "));

  return;
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let size = null;
let A = null;
let B = null;

rl.on("line", (line) => {
  if (!size) {
    size = line.split(" ").map((e) => +e);
  } else if (!A) {
    A = line.split(" ").map((e) => +e);
  } else {
    B = line.split(" ").map((e) => +e);
    rl.close();
  }
}).on("close", () => {
  solution(A, B);
  process.exit();
});
// 백준:투포인터 이용
