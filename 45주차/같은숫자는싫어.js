function solution(arr) {
  var s = [];
  for (let i of arr) {
    if (s.length == 0) s.push(i);
    else {
      var end = s[s.length - 1];
      if (end != i) s.push(i);
    }
  }
  console.log(s);

  return s;
}
// 프로그래머스 Js문제
