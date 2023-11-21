function solution(s) {
  var answer = 0;
  let arr = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  arr.forEach((v, i) => {
    let arr = s.split(v); // ex) s가 one4one 이고, 'one'에 대해서 split 하면 -> ['',4,''] 나옴.
    s = arr.join(i); // i가 곧 교체할 숫자로 사용될 수 있으므로, join사용.
  });

  return parseInt(s);
}
// 프로그래머스 문제
