const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  arr.sort((a, b) => a - b);

  console.log(arr[k - 1]);
};

let [n, k] = [null, null];

let arr;

rl.on("line", (line) => {
  if (!n) [n, k] = line.split(" ").map((e) => +e);
  else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 k번째 수.
