const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const dx = [0, -1, 0, 1];
const dy = [-1, 0, 1, 0];
const solution = () => {
  let nxtBigSize = 0;
  const dfs = (x, y, num) => {
    // dfs로 각 방의 개수 구하기.
    visited[x][y] = num;
    let ret = 1;
    for (let i = 0; i < 4; i++) {
      if (!(g[x][y] & (1 << i))) {
        // 벽이 있나 체크.
        const [nx, ny] = [x + dx[i], y + dy[i]]; // 벽이 없으니, 해당 방향으로 이동.
        if (visited[nx][ny]) continue; // 방문 안한곳 방문.
        visited[nx][ny] = num; // 방번호 표시.
        ret += dfs(nx, ny, num); // ret을 반환하면서 방크기 계속 더하기.
      }
    }

    return ret; // 각 방의 넓이 반환.
  };

  // 각 방 만들기. (덩어리 만들기.)
  const visited = Array(n)
    .fill()
    .map((e) => Array(m).fill(0));
  const rooms = [0]; // 각 num번 방의 상태정보 위치.
  let roomCnt = 0;
  let num = 1; // 방번호.
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (!visited[x][y]) {
        rooms.push(dfs(x, y, num)); //
        num += 1;
        roomCnt += 1;
      }
    }
  }
  // 벽을 부쉈을 때, 합쳐진 방의 크기 최대값 구하기. => visited 배열에서 표시한 방번호를 가지고, 인접한 방의 정보를 가지고 구한다.
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      for (let i = 0; i < 4; i++) {
        const [nx, ny] = [x + dx[i], y + dy[i]];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
          let [a, b] = [visited[x][y], visited[nx][ny]]; // 서로 다른 두 방 번호.
          if (a !== b) nxtBigSize = Math.max(nxtBigSize, rooms[a] + rooms[b]);
        }
      }
    }
  }
  console.log(roomCnt); // 총 방의 개수
  console.log(Math.max(...rooms)); // 가장 큰 방 넓이
  console.log(nxtBigSize); // 벽을 하나 부쉈을 때 가장 큰 방 넓이.
};
let [n, m] = [null, null];
let g = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) [m, n] = line.split(" ").map((e) => +e);
  else {
    g.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 성곽.
// dfs/bfs + bismasking
