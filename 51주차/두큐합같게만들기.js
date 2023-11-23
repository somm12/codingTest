function solution(queue1, queue2) {
  let answer = 0;
  let n = queue1.length;
  let arr = [...queue1, ...queue2]; // 두 큐를 이어 붙이기
  let [idx1, idx2] = [0, n]; // 두 지점을 초기화. 각각 큐1과 큐2가 시작되는 지점.
  let sum1 = queue1.reduce((acc, cur) => {
    return (acc += cur);
  }, 0);
  let sum2 = queue2.reduce((acc, cur) => {
    return (acc += cur);
  }, 0);

  let goal = sum1 + sum2;
  if (goal % 2 !== 0) return -1;
  goal /= 2; // 목표로하는 값.
  while (idx1 < 2 * n && idx2 < 2 * n) {
    // 이어 붙이 배열의 길이 보다 작을 때 까지.
    if (sum1 === goal) {
      return answer;
    }
    if (sum1 < goal) {
      // 목표보다 작다면, 큐2에 있는 부분 더하고, idx2 증가
      sum1 += arr[idx2];
      idx2 += 1;
    } else {
      // 목표보다 크다면, 큐1에 있는 제일 앞 원소는 빼주고 idx1 증가, ** 맨뒤로 push.
      const tmp = arr[idx1];
      arr.push(tmp); // 맨뒤로 보내주기.
      sum1 -= arr[idx1];
      idx1 += 1;
    }
    answer += 1; // 횟수는 1씩 증가.
  }
  return -1;
}
// 프로그래머스 문제.
// 슬라이딩 윈도우.
