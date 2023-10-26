function solution(a, b) {
  var answer = 0;
  const tmp1 = parseInt(a.toString() + b.toString());
  const tmp2 = parseInt(b.toString() + a.toString());

  return tmp2 > tmp1 ? tmp2 : tmp1;
}
