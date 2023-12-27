function solution(board, skill) {
  var answer = 0;
  const [n, m] = [board.length, board[0].length];
  const arr = Array(n + 1)
    .fill()
    .map((e) => Array(m + 1).fill(0));
  for (let [type, r1, c1, r2, c2, degree] of skill) {
    if (type === 1) degree *= -1;
    arr[r1][c1] += degree;
    arr[r2 + 1][c2 + 1] += degree;
    arr[r1][c2 + 1] += degree * -1;
    arr[r2 + 1][c1] += degree * -1;
  }
  //행기준
  for (let x = 0; x < n; x++) {
    let total = 0;
    for (let y = 0; y < m; y++) {
      total += arr[x][y];
      arr[x][y] = total;
    }
  }
  //열 기준
  for (let y = 0; y < m; y++) {
    let total = 0;
    for (let x = 0; x < n; x++) {
      total += arr[x][y];
      arr[x][y] = total;
    }
  }

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      board[x][y] += arr[x][y];
      if (board[x][y] > 0) answer += 1;
    }
  }
  return answer;
}
// 프로그래머스
// 누적합 이용 문제.
// 해당 범위 까지 일반 반복문으로 값을 더해나가면 시간초과 발생
// x1,y1, x2,y2 범위에 n만큼 변화가 있다면
// => x1,y1, x2+1,y2+1 : +n
// => x1,y2+1, x2+1, y1 : -n 더하기.
// 그리고 누적합을 행마다, 열마다하면 한번에 누적 연산을 할 수 있어서 board를 합치면 결과가 나옴.
