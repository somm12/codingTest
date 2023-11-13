function solution(board) {
  let N = board.length;
  const dp = Array(N)
    .fill()
    .map((e) =>
      Array(N)
        .fill()
        .map((e) => Array(4).fill(Infinity))
    );

  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const q = [
    [0, 0, 1, 0],
    [0, 0, 3, 0],
  ];
  const inRange = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < N;
  };

  while (q.length) {
    const [x, y, pDir, cost] = q.shift();
    // console.log(x,y,"!")
    dirs.forEach(([dx, dy], nextDir) => {
      const [nx, ny] = [x + dx, y + dy];
      if (inRange(nx, ny) && board[nx][ny] === 0) {
        const nextCost = cost + (pDir === nextDir ? 100 : 600);
        if (nextCost < dp[nx][ny][nextDir]) {
          dp[nx][ny][nextDir] = nextCost;
          q.push([nx, ny, nextDir, nextCost]);
        }
      }
    });
  }
  return Math.min(...dp[N - 1][N - 1]);
}
// 프로그래머스
// dp + bfs 이용.
// 각 지점에서의 현재 방향에 따라 드는 비용이 다르므로, 3차원 배열을 이용해서 비용을 담는다.
// 더 최소 비용의 경우가 아니라면, 넘어감.
// 코너가 생기는 부분에는 직선도로+코너도로 합쳐지는 비용이 생겨서 600원으로 둠.
