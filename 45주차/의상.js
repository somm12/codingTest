function solution(clothes) {
  var answer = 1;
  var dict = {};
  for (let c of clothes) {
    let name = c[0];
    let kind = c[1];
    if (kind in dict) dict[kind] += 1;
    else dict[kind] = 1;
  }
  for (let kind in dict) {
    answer *= dict[kind] + 1;
  }
  return answer - 1;
}

// 플그머 고득점 kit 해시 - 의상 문제
