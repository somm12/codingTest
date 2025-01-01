const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let cnt = 0;
let answer = 0;
let [n, m] = [null, null];
const S = new Set();
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    if (cnt < n) {
      S.add(line);
    } else {
      if (S.has(line)) {
        // set 자료구조로 집합에 속한 문자열 구하기.
        answer += 1;
      }
    }
    cnt += 1;
    if (cnt === n + m) rl.close();
  }
});
rl.on("close", () => {
  console.log(answer);
  process.exit();
});
// 백준 문자열 집합.
