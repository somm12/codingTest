const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  const ans = [];

  const dfs = (start, res) => {
    if (ans.length > 0) return;
    if (res.length === 2) {
      let tmp = res[0] + res[1];
      if (total - tmp === 100) {
        ans.push(...res);
      }
      return;
    }
    for (let i = start; i < 9; i++) {
      dfs(i + 1, [...res, arr[i]]);
    }
  };
  dfs(0, []); // 전체 합 - 2요소의 합 === 100인 경우 찾기.
  const answer = arr.filter((v) => !ans.includes(v)); // 전체 배열에서, 해당 요소에 포함되지 않는 난쟁이 가져오기
  answer.sort((a, b) => a - b); // 오름차순 정렬
  console.log(answer.join("\n"));
};

let cnt = 0;
let total = 0;
const arr = [];
rl.on("line", (line) => {
  if (cnt < 9) {
    arr.push(+line);
    total += +line;
    cnt += 1;
    if (cnt === 9) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
//백준 일곱 난쟁이
