const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const [a, b] = line.split(" ").map((e) => +e);
  if (a == 0 && b == 0) rl.close();
  if (a % b == 0) console.log("multiple");
  else if (b % a == 0) console.log("factor");
  else console.log("neither");
});
rl.on("close", () => {
  process.exit();
});
// 백준 배수와 약수
