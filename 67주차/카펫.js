function solution(brown, yellow) {
  var answer = [];

  let sum = brown + yellow;
  for (let h = 3; h <= brown; h++) {
    let w = sum / h;
    if (sum % h == 0 && (h - 2) * (w - 2) === yellow) return [w, h];
  }
}
