function solution(myString) {
  var answer = "";
  for (let s of myString) {
    if (s === "a") {
      answer += "A";
    } else if (s.toUpperCase() === s && s !== "A") {
      // 대문자 이면서 A가 아니면
      answer += s.toLowerCase();
    } else {
      answeR += s;
    }
  }
  return answer;
}
// 프로그래머스 문제.
