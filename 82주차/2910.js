const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const info = {};
  for (let i = 0; i < N; i++) {
    const v = arr[i];
    if (v in info) {
      info[v][0] += 1;
    } else info[v] = [1, i];
  }
  const tmp = arr.map((v) => [v, info[v][0], info[v][1]]);
  tmp.sort((a, b) => {
    if (a[1] !== b[1]) return b[1] - a[1];
    return a[2] - b[2];
  });

  const answer = tmp.map((v) => v[0]);
  console.log(answer.join(" "));
};

let [N, C] = [null, null];
let arr = null;

rl.on("line", (line) => {
  if (!N) {
    [N, C] = line.split(" ").map((e) => +e);
  } else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 빈도 정렬.
