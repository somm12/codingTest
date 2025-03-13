function solution(cards1, cards2, goal) {
  var answer = "Yes";
  let idx = 0;
  while (idx < goal.length) {
    let flag = false;
    if (cards1.length > 0 && cards1[0] === goal[idx]) {
      cards1.shift();
      flag = true;
      idx += 1; // 다음 goal 문자열을 비교한다.
    } else if (cards2.length > 0 && cards2[0] === goal[idx]) {
      cards2.shift();
      flag = true;
      idx += 1;
    }

    if (idx < goal.length && flag === false) {
      answer = "No";
      break;
    }
  }
  return answer;
}
//프로그래머스 연습문제
