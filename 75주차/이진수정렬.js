const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N;
let K;
let data = [];

const sol = () => {
  const tmp = [];
  for (let v of data) {
    const bin = v.toString(2); // 2진법으로 바꾸기.
    let cnt = 0;
    for (let x of bin) {
      if (x == "1") cnt += 1;
    }
    tmp.push([cnt, v]);
  }
  tmp.sort((a, b) => {
    if (a[0] !== b[0]) return b[0] - a[0]; // 내림차순
    return b[1] - a[1]; // 내림차순.
  });

  console.log(tmp[K - 1][1]);
};
rl.on("line", (line) => {
  if (!N) {
    [N, K] = line.split(" ").map((e) => +e);
  } else {
    data = line.split(" ").map((e) => +e);
    rl.close();
  }
});

rl.on("close", () => {
  sol();
  process.exit();
});
