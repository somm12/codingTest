function solution(participant, completion) {
  var answer = "";
  var dict = {};
  for (let name of participant) {
    if (name in dict) dict[name] += 1;
    else dict[name] = 1;
  }
  for (let name of completion) {
    dict[name] -= 1;
  }
  for (let name in dict) {
    if (dict[name] > 0) {
      answer = name;
      break;
    }
  }

  return answer;
}
// 프로그래머스 고득점 kit - 해시 js문제
