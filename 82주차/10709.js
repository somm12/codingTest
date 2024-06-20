const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const answer = Array(n)
    .fill()
    .map((e) => Array(m).fill(-1));
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (arr[x][y] == "c") {
        // 바로 구름이 있으므로, 다음 칸 탐색.
        answer[x][y] = 0;
        continue;
      }
      let num = 0;

      for (let j = y; j >= 0; j--) {
        // 가장 가까운 곳에 구름 있는 지점 찾기. 찾으면 break하고 다음 칸 탐색.
        if (arr[x][j] == "c") {
          answer[x][y] = num;
          break;
        }
        num += 1;
      }
    }
  }
  for (let x = 0; x < n; x++) {
    console.log(answer[x].join(" "));
  }
};
let arr = [];
let [n, m] = [null, null];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) [n, m] = line.split(" ").map((e) => +e);
  else {
    arr.push(line);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 기상캐스터
