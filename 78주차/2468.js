// 물에 잠기지 않는 안전한 영역 최대! 개수 찾기.
// 1. 최솟값 ~ 최댓값 찾기
// 2. for문으로 해당 값 이하는 전부. -1 넣기. => 원래 배열 복사. 방문 배열 초기화.(sink 함수.)
// 3. -1 아닌 거 덩어리 만들기. (counting 함수)
// 4. couting 함수 반환 값 업데이트.

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const [dx, dy] = [
  [-1, 1, 0, 0],
  [0, 0, -1, 1],
];

const bfs = (x, y, tmp, visited, h) => {
  visited[x][y] = 1;
  const q = [];
  q.push([x, y]);
  while (q.length > 0) {
    const [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (!visited[nx][ny] && tmp[nx][ny] > h) {
          visited[nx][ny] = 1;
          q.push([nx, ny]);
        }
      }
    }
  }
};
const counting = (h, tmp) => {
  const visited = Array(n)
    .fill()
    .map((e) => Array(n).fill(0));
  let ret = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (!visited[i][j] && tmp[i][j] > h) {
        // h개 보다 큰 것 세기
        bfs(i, j, tmp, visited, h);
        ret += 1;
      }
    }
  }
  return ret;
}; // -1 아닌거 덩어리 구하기

const solution = () => {
  let maxV = 0;
  let minV = 100;
  let answer = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      maxV = Math.max(maxV, g[i][j]);
      minV = Math.min(minV, g[i][j]);
    }
  }
  for (let h = minV - 1; h < maxV; h++) {
    // 최대 안전영역 개수이므로, 최솟값 -1 부터 최댓값 미만까지 잠기는 높이 설정.
    // 100
    const tmp = g.map((arr) => [...arr]); // 원본 배열 복사.

    answer = Math.max(counting(h, tmp), answer); // h이하를 제외한 안전영역의 개수 구하기.
  }
  console.log(answer);
};
let n = null;
let g = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
