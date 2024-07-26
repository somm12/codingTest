const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  let answer = 1;
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  const dfs = (x, y, num, L) => {
    // A ~ Z를 각각 26자리의 이진수로 표현한다고 했을 때, 해당 idx에서 비트를 키고 끄고를 이용해서 방문처리하기.
    answer = Math.max(answer, L);
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
        let nxt = 1 << (g[nx][ny].charCodeAt() - 65); // 1000 방식으로 켜기.

        if ((num & nxt) == 0) {
          // 만약 and 연산 값이 0이라면 방문하지 않았다는 뜻.
          dfs(nx, ny, num | nxt, L + 1);
        }
      }
    }
  };

  dfs(0, 0, 1 << (g[0][0].charCodeAt() - 65), 1);
  console.log(answer);
};

let [n, m] = [null, null];
let g = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) [n, m] = line.split(" ").map((e) => +e);
  else {
    g.push(line.split(""));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 알파벳. 비트마스킹 활용해보기.
