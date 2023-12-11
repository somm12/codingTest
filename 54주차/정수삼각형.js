function solution(triangle) {
  var answer = 0;
  for (let i = 1; i < triangle.length; i++) {
    for (let j = 0; j < triangle[i].length; j++) {
      if (j === 0) {
        // 맨 앞쪽은 바로 이전 행의 맨 앞 값이 계속 더해짐
        triangle[i][j] += triangle[i - 1][j];
      } else if (j === triangle[i].length - 1) {
        // 행의 마지막 부분은 이전 행의 마지막 부분 값이 계속 더해짐
        triangle[i][j] += triangle[i - 1][j - 1];
      } else {
        // 나머지 중간 부분은 이전 행의 이전 열, 같은열 중 큰 값과 더하기
        triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
      }
    }
  }
  // 마지막 행 중, 가장 큰 값이 최댓값.
  let maxV = -1;
  triangle[triangle.length - 1].forEach((v) => {
    if (maxV < v) maxV = v;
  });
  return maxV;
}
// 프로그래머스 문제
