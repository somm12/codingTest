function solution(N, number) {
  var answer = -1;
  const arrSet = [];
  if (N === number) return 1;
  arrSet[1] = new Set().add(N);
  for (let i = 2; i < 9; i++) {
    cal(i);
    if (arrSet[i].has(number)) {
      answer = i;
      break;
    }
  }
  function cal(cnt) {
    arrSet[cnt] = new Set();
    arrSet[cnt].add(+N.toString().repeat(cnt));
    for (let i = 1; i < cnt; i++) {
      const [left, right] = [i, cnt - i];
      for (const l of arrSet[left]) {
        for (const r of arrSet[right]) {
          arrSet[cnt].add(l + r);
          arrSet[cnt].add(l - r);
          arrSet[cnt].add(l * r);
          if (r !== 0) {
            arrSet[cnt].add(Math.floor(l / r));
          }
        }
      }
    }
  }

  return answer;
}
// 프로그래머스
// n으로 표현
// 1개 -> 5
// 2개 -> 55, 1개일때 경우끼리(사칙 연산)
// 3개 -> 1개 2개 (사칙연산), 2개 1개 (사칙연산)
// 4개 -> 1개 3개, 2개 2개, 3개 1개 ..
//....
// 각 x개 일때 나올 수 있는 숫자를 계산하고 중복을 위해 set을 사용. 값이 number가 나온다면 return
