function solution(n, cores) {
  const len = cores.length;

  var rest = n - len; // 남은 작업 개수(초반에 항상 len개 만큼 작업이 각 코어에 할당됨.)
  let left = 1; // 작업처리 시간대
  let right = (Math.max(...cores) * rest) / len; // 작업 처리하는데 걸리는 최대 시간 대.
  // 마지막 작업을 처리하는 시간과 가장 가까운 시간대 찾기.
  while (left < right) {
    const mid = ((left + right) / 2) >> 0; // 중간 값. 작업 처리 시간대
    let capacity = 0; // 총 작업 량.

    for (const core of cores) {
      capacity += (mid / core) >> 0; // 코어의 작업 처리 시간이 처리 시간대의 약수 일때, 작업을 수행.(그 수 만큼 작업 처리)
    }

    if (capacity >= rest) {
      // 남은 작업 처리이상이라면, 범위 좁히기.
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  // right은 마지막 작업 처리한 시간대와 가장 가까운 큰 값.
  for (const core of cores) {
    rest -= ((right - 1) / core) >> 0; // 이전 시간 때 까지의 작업량을 빼주어 남은 작업량 구하기.
  }

  for (let i = 0; i < len; i++) {
    // 남은 작업처리량이 0이 되는 순간 찾기.
    if (right % cores[i] === 0) {
      rest -= 1;
      if (!rest) {
        return i + 1;
      }
    }
  }
}
