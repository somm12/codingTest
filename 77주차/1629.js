const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [a, b, c] = [null, null, null];
rl.on("line", (line) => {
  if (!a) {
    [a, b, c] = line.split(" ").map((e) => +e);

    rl.close();
  }
});

rl.on("close", () => {
  console.log(solution(a, b, c));
  process.exit();
});
const solution = (A, B, C) => {
  A = BigInt(A); // 2^53-1 보다 큰 수를 다룰 때 쓰이는 형 변환 함수 BigInt.
  C = BigInt(C);
  const pow = (exponent) => {
    // (a*b)%c == (a%c) * (b%c) 이용해서 반으로 쪼개기
    // => b가 1일 때까지 수행하면 연산 횟수는 시간 복잡도 logN.
    // 홀수 일 때 짝수 일 때 경우가 다르다.
    // 10^11 % 12
    // = ((10^5)%12 x (10^5)%12 x 10)% 12
    if (exponent === 1) return A % C;
    const half = pow(parseInt(exponent / 2));
    if (exponent % 2 === 0) return (half * half) % C;
    return (half * half * A) % C;
  };
  return pow(B).toString();
};
// 백준 곱셈
