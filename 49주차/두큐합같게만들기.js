function solution(queue1, queue2) {
  var answer = 0;
  const arr = [...queue1, ...queue2];
  const sum = (arr) => arr.reduce((a, b) => a + b); // 전체 합을 구하는 함수.
  let start = 0;
  let end = queue1.length;
  let total = sum(arr.slice(start, end));
  const target = sum(arr) / 2; // 만들고자하는 합.

  const maxCnt = queue1.length * 3; // start는 2*n만큼, end는 n만큼 이동가능하므로 총 3*n 만큼이동.
  while (answer <= maxCnt) {
    if (total < target) {
      // 타겟보다 작으면 end +1
      total += arr[end];
      end++;
    } else if (total === target) return answer;
    else {
      total -= arr[start]; // 타겟보다 크다면 start + 1
      start++;
    }
    answer += 1;
  }

  return -1; // 같게 만들어지지 않으면 -1.
}
// 프로그래머스 문제
// 투포인터를 이용해서 js로 구현.
