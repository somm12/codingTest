function solution(n, money) {
  const dp = Array(n + 1).fill(0);
  dp[0] = 1;
  for (let i = 0; i < money.length; i++) {
    const coin = money[i];
    for (let j = coin; j <= n; j++) {
      dp[j] += dp[j - coin] % 1000000007;
    }
  }

  return dp[n];
}
// dp[x]원. x원을 만들 수 있는 경우의 수
// dp[j-coin] => j원을 coin 거스름돈으로 만들 수 있는 경우의 수 즉, 뺀 금액의 수 + coin과 같음.
