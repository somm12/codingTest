function solution(progresses, speeds) {
  var answer = [];
  var q = [];
  for (let i = 0; i < progresses.length; i++) {
    q.push(Math.ceil((100 - progresses[i]) / speeds[i])); // 남을 일수 구하기.
  }
  console.log(q);
  while (q.length > 0) {
    var s = [];
    var target = q.shift();
    s.push(target);
    while (q && target >= q[0]) {
      //한번 배포될 때, 여러개 배포체크를 위해 s에 push.
      s.push(q.shift());
    }
    answer.push(s.length);
  }
  return answer;
}
// 프로그래머스 js로 풀기.
