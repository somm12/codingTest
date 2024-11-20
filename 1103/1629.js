const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  A = BigInt(A);
  C = BigInt(C);

  const mul = (exponent) => {
    if (exponent === 1) return A % C;
    const half = mul(Math.floor(exponent / 2));
    if (exponent % 2 === 0) return (half * half) % C;
    return (half * half * A) % C;
  };
  console.log(mul(B).toString());
};

let [A, B, C] = [null, null, null];
rl.on("line", (line) => {
  if (!A) {
    [A, B, C] = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 곱셈.
