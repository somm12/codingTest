function solution(sizes) {
  var answer = 0;
  sizes = sizes.map((v) => v.sort((a, b) => a - b)); // 각 배열 내 순서대로 정렬.

  let [mw, mh] = [0, 0];
  sizes.forEach((v) => {
    // 가장 크고 너비 높이 찾기.
    mw = Math.max(mw, v[0]);
    mh = Math.max(mh, v[1]);
  });

  return mw * mh;
}
// 프로그래머스 최소 직사각형.
