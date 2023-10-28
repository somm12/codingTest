function solution(msg) {
  var answer = [];
  let dict = {};
  for (let i = 0; i < 26; i++) {
    dict[String.fromCharCode(65 + i)] = i + 1;
  }
  let idx = 0;
  let w = "";
  let num = 27;
  const n = msg.length;

  while (idx < n) {
    w += msg[idx];
    if (dict[w]) idx += 1;
    else {
      const tmp = w.slice(0, w.length - 1);
      answer.push(dict[tmp]);
      dict[w] = num;
      num += 1;
      w = "";
    }
  }
  if (w.length > 0) answer.push(dict[w]);
  return answer;
}
// 프로그래머스 문제.
