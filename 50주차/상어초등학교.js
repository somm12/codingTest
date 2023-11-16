let dx = [-1, 1, 0, 0];
let dy = [0, 0, -1, 1];
const inRange = (nx, ny) => {
  // 범위 내인지 확인.
  return 0 <= nx && nx < N && 0 <= ny && ny < N;
};
const getScore = (g, like) => {
  // 총 점수 계산.
  let total = [];
  let answer = 0;
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      let cnt = 0;
      for (let i = 0; i < 4; i++) {
        const [nx, ny] = [x + dx[i], y + dy[i]];
        if (inRange(nx, ny) && like[g[x][y]].includes(g[nx][ny])) cnt += 1;
      }
      if (cnt > 0) total.push(cnt);
    }
  }
  total.forEach((v) => (answer += 10 ** (v - 1)));
  return answer;
};

const solution = (N, like, arr) => {
  const g = Array(N) // 2차원 배열 0으로 초기화.
    .fill()
    .map((e) => Array(N).fill(0));

  arr.forEach((num) => {
    let cand = [];
    for (let x = 0; x < N; x++) {
      for (let y = 0; y < N; y++) {
        if (g[x][y] === 0) {
          let [cnt, empty] = [0, 0];
          for (let i = 0; i < 4; i++) {
            let [nx, ny] = [x + dx[i], y + dy[i]];
            if (inRange(nx, ny)) {
              if (like[num].includes(g[nx][ny])) cnt += 1;
              else if (g[nx][ny] === 0) empty += 1;
            }
          }
          cand.push([cnt, empty, x, y]);
        }
      }
    }
    cand.sort((a, b) => {
      // 좋아하는 사람 수 많고>빈칸 많고>행이 작고>열이 작은 순.
      if (a[0] !== b[0]) return b[0] - a[0];
      else if (a[1] !== b[1]) return b[1] - a[1];
      else if (a[2] !== b[2]) return a[2] - b[2];
      return a[3] - b[3];
    });
    let [a, b, x, y] = cand[0];
    g[x][y] = num;
  });

  console.log(getScore(g, like));
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;
let count = 0;
let data = null;
let like = {};
let arr = []; // 순서를 담을 배열

rl.on("line", (line) => {
  if (!N) {
    N = +line;
  } else if (!data) {
    data = line.split(" ").map((e) => +e);
    arr.push(data[0]);
    like[data[0]] = data.slice(1, 5);
    data = null;
    count += 1;
  }
  if (count === N * N) rl.close();
}).on("close", () => {
  solution(N, like, arr);
  process.exit();
});
// js로 백준 구현 문제 풀기.
