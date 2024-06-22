const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let [A, B] = [0, 0];
  let prev = 0;
  let [t1, t2] = [0, 0];
  for (const [num, time] of arr) {
    // 서로 시간대 사이에 이미 이기고 있다면, 이긴 시간 업데이트. ex) 동점이 되는 순간 이전에는 이기고 있었음.
    if (A < B) t2 += time - prev;
    else if (A > B) t1 += time - prev;
    if (num == 1) A += 1;
    else B += 1;
    prev = time; // 최신 이전 시간 업데이트.
  }
  if (A > B) t1 += 48 * 60 - prev;
  // 마지막 48분 시간 처리.
  else if (A < B) t2 += 48 * 60 - prev;

  let [m1, s1] = [
    parseInt(t1 / 60)
      .toString()
      .padStart(2, 0),
    (t1 % 60).toString().padStart(2, 0),
  ];
  let [m2, s2] = [
    parseInt(t2 / 60)
      .toString()
      .padStart(2, 0),
    (t2 % 60).toString().padStart(2, 0),
  ];

  console.log(`${m1}:${s1}`);
  console.log(`${m2}:${s2}`);
};
let n = null;
let cnt = 0;
let arr = [];
rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    let [num, t] = line.split(" ");
    num = +num;
    let [h, m] = t.split(":").map((e) => +e);
    t = h * 60 + m;
    arr.push([num, t]);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 NBA 농구.
