function solution(stones, k) {
  let left = 1;
  let right = 200000000;
  let answer = 0;
  while (left <= right) {
    const mid = parseInt((left + right) / 2);
    let cnt = 0;
    let flag = true;
    for (let i = 0; i < stones.length; i++) {
      if (stones[i] - mid < 0) {
        cnt += 1;
      } else cnt = 0;
      if (cnt === k) {
        // 음수가 k개 이상 부터는 불가능!!
        flag = false;
        break;
      }
    }
    if (flag) {
      // 최댓값을 구하는 것이므로, 마지막 mid가 최대이다. answer에 저장.
      left = mid + 1;
      answer = mid;
    } else {
      // 범위 줄이기
      right = mid - 1;
    }
  }

  return answer;
}
