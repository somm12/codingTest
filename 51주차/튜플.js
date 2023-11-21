function solution(s) {
  var answer = [];
  let set = new Set();

  s = s.slice(2, s.length - 2);
  s = s.split("},{");
  s = s.map((v) => v.split(",").map((e) => +e));

  s.sort((a, b) => a.length - b.length);
  s.forEach((arr) => {
    arr.forEach((v) => set.add(v));
  });

  return [...set];
}
// 프로그래머스.
