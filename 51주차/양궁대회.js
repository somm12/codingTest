function solution(n, info) {
  var answer = [];
  const dfs = (L, total, a, r, arr) => {
    if (L === 11) {
      // 마지막 발까지 갔다면, 라이언 점수가 더 높으면 answer에 후보 넣기.
      if (a < r) answer.push([r - a, ...arr]);
      return;
    }
    // info[L]+1 or 0 발을 쏘기 때문에 마지막에 총 n발 개수를 맞춰야 함!
    if (total + info[L] + 1 <= n) {
      // 어피치보다 +1발 더쏴도 n발 넘게 쏘지 않는다면
      dfs(L + 1, total + info[L] + 1, a, r + 10 - L, [...arr, info[L] + 1]);
    }
    // 쏘지 않기. 어피치가 이김(하지만 어피치가 0개를 쐈다면 점수 없음.)
    if (info[L] > 0) dfs(L + 1, total, a + 10 - L, r, [...arr, 0]);
    else dfs(L + 1, total, a, r, [...arr, 0]);
  };
  dfs(0, 0, 0, 0, []);
  if (answer.length == 0) return [-1]; // 이길 수 없는 경우.
  answer.sort((a, b) => {
    if (a[0] !== b[0]) return b[0] - a[0]; // 점수차이가 큰 순.
    for (let i = 11; i >= 1; i--) {
      // 차례대로 낮은점수가 많은 순.
      if (a[i] !== b[i]) return b[i] - a[i];
    }
  });

  answer = answer[0].slice(1, 12); // 각 점수 몇 발 쐈는지 배열 반환.
  let sum = answer.reduce((acc, cur) => {
    return (acc += cur);
  }, 0);
  if (sum < n) answer[answer.length - 1] = n - sum; // 만약 정답에서 총 n발보다 작으면 0점에 추가.
  return answer;
}
// 프로그래머스
