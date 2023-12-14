function solution(m, n, puddles) {
  let dp = Array(n + 1) // 행과 열 부분에 padding 주기.
    .fill()
    .map((e) => Array(m + 1).fill(0));

  puddles.forEach(([x, y]) => {
    dp[y][x] = 1;
  });
  dp[0][1] = 1; // 맨 처음, 집이 위치한 (1,1)값은 1이 되어야하므로, 1을 할당해둔다.
  for (let x = 1; x <= n; x++) {
    for (let y = 1; y <= m; y++) {
      if (dp[x][y]) dp[x][y] = 0;
      // 웅덩이가 있는 곳은 0 으로 할당해서 넘어감.(이후에 더해져도 없는셈 칠 수 있음.)
      else {
        dp[x][y] = dp[x - 1][y] + dp[x][y - 1]; // 위쪽 또는 왼쪽으로부터 올 수 있음.
        if (dp[x][y] > 1000000007) dp[x][y] %= 1000000007;
      }
    }
  }
  return dp[n][m];
}
