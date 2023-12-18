function solution(sticker) {
  let answer = 0;

  const n = sticker.length + 2; // index out of range 피하기 위함.
  const dp1 = Array(n).fill(0);
  const dp2 = Array(n).fill(0);

  if (sticker.length === 1) return sticker[0];

  // 첫번째 원소 포함했을 때. 마지막 원소는 포함 X기 때문에 n-1 까지만.
  for (let i = 2; i < n - 1; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + sticker[i - 2]);
  }
  // 첫번째 원소 불포함. 마지막 원소 포함 가능.
  for (let i = 3; i < n; i++) {
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i - 2]);
  }

  return Math.max(dp1[n - 2], dp2[n - 1]);
}
// 프로그래머스
// 첫번째와 마지막은 연결 되어 있음. 첫번째를 뜯는지, 아닌지에 따라 두 가지 dp를 구한다.
