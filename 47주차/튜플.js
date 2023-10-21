function solution(s) {
  var answer = [];
  let arr = s.slice(2, s.length - 2).split("},{");

  arr = arr.map((v, i) => {
    return v.split(",");
  });
  let tmp = [];
  for (a of arr) {
    a = a.map((v, i) => {
      return parseInt(v);
    });
    tmp.push(a);
  }

  tmp.sort((a, b) => {
    // 배열 길이가 작은 순으로 정렬.
    return a.length - b.length;
  });

  let dict = new Set();
  for (let arr of tmp) {
    for (let v of arr) {
      if (!dict.has(v)) {
        // 없으면,
        dict.add(v);
      }
    }
  }
  answer = [...dict];
  return answer;
}
// 프로그래머스 - 카카오 튜플.
