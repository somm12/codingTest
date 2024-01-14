function solution(scores) {
  var answer = 0;
  const arr = scores.map(([a, b], i) => {
    return { index: i, a: a, b: b };
  });

  arr.sort((x, y) => {
    // 첫번째 원소 내림차순, 2번째 원소 기준 오름 차순 정렬.
    if (x.a !== y.a) return y.a - x.a;
    return x.b - y.b;
  });
  let maxA = arr[0].a;
  let maxB = -1;
  let tmp = [];
  for (let v of arr) {
    maxB = Math.max(maxB, v.b);
    if (v.a < maxA && v.b < maxB) continue; // 값이 둘다 작다면 제외 시키기.
    tmp.push([v.index, v.a + v.b]);
  }
  tmp.sort((a, b) => b[1] - a[1]);
  console.log(tmp);
  for (let i = 0; i < tmp.length; i++) {
    if (tmp[i][0] === 0) return i + 1; // 완호 등수 반환
  }

  return -1;
}
