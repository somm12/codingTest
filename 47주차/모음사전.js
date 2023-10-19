function solution(word) {
  var answer = 0;
  let cnt = 1;
  let arr = ["A", "E", "I", "O", "U"];
  let dict = {};

  function dfs(s) {
    if (s.length > 5) return;
    if (s.length > 0 && s.length <= 5) {
      dict[s] = cnt;
      cnt += 1;
    }

    for (let v of arr) dfs(s + v);
  }
  dfs("");

  return dict[word];
}
// 프로그래머스 완전탐색. js로 풀기.
