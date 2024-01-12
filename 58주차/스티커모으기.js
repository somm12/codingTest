function solution(sticker) {
  const n = sticker.length + 2;
  const dp1 = Array(n).fill(0); // 첫 번째 스티커를 뜯었을 때, i번째 까지 스티커의 최대 합을 담을 배열.
  const dp2 = Array(n).fill(0); // 첫 번째 스티커를 뜯지 않았을 때.

  if (sticker.length === 1) return sticker[0];
  for (let i = 2; i < n - 1; i++) {
    // 마지막 스티커도 같이 뜯기므로 n-1까지 반복.
    // 인덱스 에러를 막기위해 padding 주기.
    // 선택하거나 안하거나 둘 중에 하나이며=> 2번째 전의 스티커의 숫자 합+현재 스티커, 이전 까지의 합 : 둘중 큰 수를 할당.
    dp1[i] = Math.max(dp1[i - 2] + sticker[i - 2], dp1[i - 1]);
  }

  for (let i = 3; i < n; i++) {
    // 두번째 스티커부터 뜯기.
    dp2[i] = Math.max(dp2[i - 2] + sticker[i - 2], dp2[i - 1]);
  }

  return Math.max(dp1[n - 2], dp2[n - 1]); // 가장 마지막 부분이 제일 큰 합.
}
