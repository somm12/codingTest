function solution(phone_book) {
  var answer = true;
  var dict = {};
  for (let s of phone_book) dict[s] = 1;

  for (let s of phone_book) {
    let tmp = "";
    for (let a of s) {
      tmp += a;
      if (tmp in dict && tmp != s) return false;
    }
  }
  return answer;
}
// 플그머 해시문제
