const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  // 가장 기차 인원이 많은 때를 구하기.
  let people = 0;
  let answer = 0;
  arr.forEach(([s, e]) => {
    people += e - s; // 기차의 인원이 모두 내려야 탈 수 있으므로 e-s(탑승 인원 - 내리는 인원 만큼 추가됨.)
    answer = Math.max(answer, people);
  });
  console.log(answer);
};

let cnt = 0;
const arr = [];

rl.on("line", (line) => {
  arr.push(line.split(" ").map((e) => +e));
  cnt += 1;
  if (cnt === 10) rl.close();
});
rl.on("close", () => {
  solution();
  process.exit();
});
//백준 지능형 기차 2
