function solution(rec, sx, sy, ex, ey) {
  const g = Array(101)
    .fill()
    .map((_) => Array(101).fill(0));
  const [dx, dy] = [
    [-1, 1, 0, 0],
    [0, 0, -1, 1],
  ];
  for (let [lx, ly, rx, ry] of rec) {
    // 좌표 두배로 늘리기. 인접한 칸으로 이동하려할 때, 실제로 이어져 있지 않은데도, 있는 경우로 넘어가는 걸 피하기 위함.
    lx *= 2;
    ly *= 2;
    rx *= 2;
    ry *= 2;
    for (let i = lx; i <= rx; i++) {
      for (let j = ly; j <= ry; j++) {
        if (i === rx || i === lx || j === ry || j === ly) {
          // 갈 수 있는 테두리 경로값을 1로 만들기
          if (g[i][j] === 1) continue;
          // 겹치는 테두리는 그래도 두기.
          else {
            g[i][j] += 1; // 1이 아닌 값 0 이나 2이상은 +1. 테두리 표시하기
          }
        } else {
          g[i][j] += 2; // 테두리 아닌 내부는 2로 넣기.
        }
      }
    }
  }

  sx *= 2;
  sy *= 2;
  ex *= 2;
  ey *= 2;

  g[sx][sy] += 100;
  let q = [[sx, sy, 0]];
  while (q.length > 0) {
    const [x, y, dist] = q.shift();
    if (x === ex && y === ey) return dist / 2;
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (0 <= nx && nx < 101 && 0 <= ny && ny < 101) {
        if (g[nx][ny] === 1) {
          q.push([nx, ny, dist + 1]);
          g[nx][ny] += 100; // 100을 더해줌으로써, 방문처리
        }
      }
    }
  }
}
