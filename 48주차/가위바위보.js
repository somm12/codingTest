function solution(rsp) {
  var answer = "";
  let dict = { 0: "5", 2: "0", 5: "2" }; // 0:바위, 2:가위, 5:보.
  for (let v of rsp) {
    answer += dict[v];
  }
  return answer;
}
//프로그래머스
