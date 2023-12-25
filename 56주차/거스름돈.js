function solution(n, money) {
  const dp = [1, ...new Array(n).fill(0)];
  //dp[x] => money들로 x원을 만들 수 있는 경우의 수
  for (let i = 0; i < money.length; i++) {
    // 3원을 가지고 5원을 만들 수있는 경우 == 2원을 가지고 만들 수 있는 경우.(3을 더한 경우와 같다)
    for (let j = money[i]; j <= n; j++) {
      // 작은 금액 부터 n까지 차곡차곡 쌓기.
      dp[j] += dp[j - money[i]]; // j라는 금액을 만들 때 -> j - 현재 화폐단위(money[i]) 경우와 같다.
    }
  }
  return dp[n] % 1000000007;
}
