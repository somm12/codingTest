function solution(n, stations, w) {
  var answer = 0;

  let arr = [];
  let s = 1; // 시작점.
  stations.forEach((v) => {
    const cnt = v - w - 1 - s + 1; // 전파가 도달하지 않는 개수
    if (cnt > 0) arr.push(cnt);
    s = v + w + 1; // 다음 도달하지 않는 부분 시작점.
  });
  if (s <= n) {
    arr.push(n - s + 1);
  }

  arr.forEach((v) => (answer += Math.ceil(v / (2 * w + 1))));

  return answer;
}
