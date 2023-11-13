const solution = (idxs, arrs) => {
  arrs.forEach((arr, i) => {
    arr = arr.map((v, i) => [i, v]);
    let nowIdx = idxs[i];

    let cnt = 1;
    while (arr.length) {
      const [idx, num] = arr.shift();
      let flag = false;

      for (let [i, tmp] of arr) {
        if (num < tmp) {
          arr.push([idx, num]);
          flag = true;
          break;
        }
      }
      if (!flag) {
        if (idx === nowIdx) {
          console.log(cnt);
          break;
        }
        cnt += 1;
      }
    }
  });
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let tc = null;
let count = 0;
let [n, nowIdx] = [null, null];
let idxs = [];
let arr = [];
rl.on("line", (line) => {
  if (!tc) {
    tc = +line;
  } else if (!n) {
    [n, nowIdx] = line.split(" ").map((e) => +e);
    idxs.push(nowIdx);
  } else {
    arr.push(line.split(" ").map((el) => +el));
    count += 1;

    n = null;
  }
  if (count === tc) {
    rl.close();
  }
}).on("close", () => {
  solution(idxs, arr);
  process.exit();
});
// 백준 문제. 우선순위가 높은것 먼저.처리
