function solution(stones, k) {
  let left = 1;
  let right = 200000000;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let flag = false;
    let cnt = 0;
    // mid만큼 시간이 지났고 했을 때, 연속되는 0의 개수 찾기
    for (let i = 0; i < stones.length; i++) {
      if (stones[i] - mid <= 0) cnt += 1;
      else cnt = 0;

      if (cnt === k) {
        // 이미 개수가 k가 되면 break.
        flag = true;
        break;
      }
    }
    // flag가 true면, 연속 0개수가 k개이상이므로, 범위를 줄여나가야한다.
    // flag가 false면,연속 0개수가 k개 미만이므로, 더 건널 수 있으므로, 정답 범위를 다시 늘린다.
    flag ? (right = mid - 1) : (left = mid + 1);
  }
  // 마지막 left가 답이 됨
  return left;
}

// 1~ 2억까지의 수가 정답 가능. 20만 * log(2억) 이므로, 시간 초과 해결 가능.
// 프로그래머스 문제
