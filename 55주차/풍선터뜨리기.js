function solution(a) {
  var answer = 0;
  const n = a.length;
  if (n <= 2) return n;
  // 원소 기준 양쪽 부분에 하나라도 자신보다 작은 수가 있다면 살아남을 수 없음.
  const left = Array(n).fill(0); // left[i] : 0~i 인덱스 까지 가장 작은 수를 담음
  const right = Array(n).fill(0); // right[i] : n-1 ~ i 인덱스 까지 가장 작은 수를 담음

  left[0] = a[0];
  right[n - 1] = a[n - 1];
  // 왼쪽 방향 기준 가장 작은 수 할당.
  for (let i = 1; i < n; i++) {
    left[i] = Math.min(left[i - 1], a[i]);
    right[n - 1 - i] = Math.min(right[n - i], a[n - 1 - i]);
  }
  // 오른쪽 방향 기준 가장 작은 수 할당.
  for (let i = 1; i < n - 1; i++) {
    if (left[i - 1] < a[i] && a[i] > right[i + 1]) continue;
    else answer += 1;
  }
  // 양쪽 끝은 무조건 살아남기 가능하므로, 2 더하기
  return answer + 2;
}
