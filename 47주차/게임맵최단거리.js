const inRange = (x, y, n, m) => {
  return 0 <= x && x < n && 0 <= y && y < m;
};
function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  let visited = new Array(n);

  for (let i = 0; i < n; i++) {
    visited[i] = new Array(m).fill(0);
  }
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  let q = [];

  q.push([0, 0]);
  visited[0][0] = 1;
  while (q.length > 0) {
    const [x, y] = q.shift();
    if (x === n - 1 && y === m - 1) break;
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (
        inRange(nx, ny, n, m) &&
        visited[nx][ny] === 0 &&
        maps[nx][ny] === 1
      ) {
        visited[nx][ny] = visited[x][y] + 1;
        q.push([nx, ny]);
      }
    }
  }
  return visited[n - 1][m - 1] > 0 ? visited[n - 1][m - 1] : -1;
}
// bfs.
