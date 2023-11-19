const solution = () => {
  data.forEach((v) => {
    if (mp.has(v)) console.log(mp.get(v));
    else console.log(input[parseInt(v) - 1]);
  });
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [N, M] = [null, null];
let data = [];
let input = [];
let [nCnt, mCnt] = [0, 0];

let mp = new Map();

rl.on("line", (line) => {
  if (!N) {
    [N, M] = line.split(" ").map((e) => +e);
  } else if (nCnt < N) {
    mp.set(line, nCnt + 1);
    input.push(line);
    nCnt += 1;
  } else if (mCnt < M) {
    data.push(line);
    mCnt += 1;
  }
  if (mCnt === M) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
//백준 Map/dict문제.
