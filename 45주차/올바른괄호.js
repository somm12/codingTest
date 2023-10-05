function solution(s) {
  var answer = true;
  var cnt = 0;
  for (let v of s) {
    if (v === ")") {
      cnt -= 1;
      if (cnt < 0) return false;
    } else cnt += 1;
  }

  return cnt === 0;
}
// 프로그래머스 Js로 풀기 - 스택. 큐
