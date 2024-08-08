const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  arr.sort((a, b) => a[0] - b[0]); // 빠른 도착 순 정렬.
  let t = arr[0][0] + arr[0][1]; // 현재 소가 입장 끝나는 시간( at+ rt )다음 시간대 도착 시간:nat과 비교해서 더하기.
  for (let i = 0; i < arr.length - 1; i++) {
    const [nat, nrt] = arr[i + 1];
    if (t <= nat) t = nat + nrt;
    else t += nrt;
  }
  console.log(t);
};
let n = null;
const arr = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 소가 길을 건너간 이유 3
