function solution(N, stages) {
  var answer = []; // [실패율, 스테이지 번호]형식.

  let total = [0];
  let sum = 0;
  let arr = Array(N + 2).fill(0);
  // 각 스테이지 별로 몇개 있는지 체크.
  stages.forEach((v) => (arr[v] += 1));

  // 총 합을 더해서 sum에 push
  for (let i = 1; i < arr.length; i++) {
    sum += arr[i];
    total.push(sum);
  }
  // total[end] - total[i-1] => 현재 스테이지에 도달한 플레이이어 수
  // arr[i] => 현재 스테이지에 도달했지만, 클리어못한 수.
  const end = total[total.length - 1];
  for (let i = 1; i < total.length - 1; i++) {
    answer.push([arr[i] / (end - total[i - 1]), i]);
  }

  answer.sort((a, b) => {
    if (a[0] !== b[0]) return b[0] - a[0];
    else a[1] - b[1];
  });
  answer = answer.map((v) => v[1]);
  return answer;
}
// 프로그래머스.
