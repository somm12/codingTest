const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const bfs = (x, visited, team) => {
  visited[x] = 1;
  let q = [];
  q.push(x);
  while (q.length > 0) {
    x = q.pop();
    for (const nx of g[x]) {
      if (!visited[nx] && team[x] == team[nx]) {
        q.push(nx);
        visited[nx] = 1;
      }
    }
  }
};
const solution = () => {
  let answer = Infinity;

  for (let i = 1; i < (1 << n) - 1; i++) {
    // 1 ~ 1111..(미만 )=> 팀 2개로 만들어져야하므로. 1 과 0 모두 섞어야 2개의 팀이 된다.
    const team = Array(n + 1).fill(0);
    let [sum1, sum2] = [0, 0];
    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) {
        // 해당 비트가 포함되면 1번팀으로.
        sum1 += arr[j + 1]; // 인구수 더하기.
        team[j + 1] = 1; // 팀 1번 표시.
      }
    }
    for (let j = 0; j < n; j++) {
      if (!team[j + 1]) {
        team[j + 1] = 2; // 팀 2번 표시.
        sum2 += arr[j + 1];
      }
    }
    const visited = Array(n + 1).fill(0);
    let cnt = 0;
    for (let j = 1; j <= n; j++) {
      // 팀이 2개로 나뉘어 지는지 확인. (똑바로 팀이 모두 연결되어 있는가 체크.)
      if (!visited[j]) {
        bfs(j, visited, team);
        cnt += 1;
      }
    }
    if (cnt == 2) {
      // 2개로 나뉘어 진다면, 인구수 차이 최솟값 업데이트.
      answer = Math.min(answer, Math.abs(sum1 - sum2));
    }
  }
  if (answer == Infinity) {
    // 여전히 무한이면 나눌 수 없는 경우이므로 -1.
    console.log(-1);
  } else console.log(answer);
};

let n = null;
let cnt = 0;
let arr = null;
let g;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
    g = Array(n + 1)
      .fill()
      .map((e) => Array());
  } else if (!arr) {
    arr = [0];
    for (const v of line.split(" ").map((e) => +e)) arr.push(v);
  } else {
    let tmp = line.split(" ").map((e) => +e);
    g[cnt + 1] = tmp.slice(1);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 게리멘더링.
