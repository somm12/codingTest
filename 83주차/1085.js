const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const [x, y, w, h] = line.split(" ").map((e) => +e);

  console.log(Math.min(Math.abs(w - x), x, Math.abs(y - h), y));
  rl.close();
});
rl.on("close", () => {
  process.exit();
});
//백준 직사각형에서 탈출.
// 경계선과 가장 가까운 거리.
