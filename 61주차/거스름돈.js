function solution(n, money) {
  const dp = [1, ...new Array(n).fill(0)]; // 자기 자신을 만들 수 있는 경우 1.
  //dp[x] => x원 만들 수 있는 경우의 수
  for (let i = 0; i < money.length; i++) {
    // a원을 가지고 b원을 만들 수있는 경우 => b - a원을 가지고 만들 수 있는 경우**
    for (let j = money[i]; j <= n; j++) {
      dp[j] += dp[j - money[i]] % 1000000007; // j라는 금액을 만들 때 -> j - 현재 화폐단위(money[i]) 경우와 같다.
    }
  }
  return dp[n];
}
// 각 화폐종류를 사용해서 차례로 n원까지 만들 수 있는 경우를 쌓아간다.
