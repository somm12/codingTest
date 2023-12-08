const solution = () => {
  let [dx, dy] = [
    [1, 0, -1, 0],
    [0, 1, 0, -1],
  ];
  let arr = [];
  let start = 0; // 시작 점
  let [tn, tm] = [N, M]; //각 테두리 마다 행과 열의 길이 범위

  let num = {}; // 번호: [x,y]좌표.
  let numCnt = 0;
  // arr에 테두리 바깥부터 arr에 넣기
  while (Math.min(tn, tm) >= 2) {
    let tmp = [];
    let [sr, sc] = [start, start]; // 시작점.
    let cnt = (tn + tm) * 2 - 4; // 바깥쪽 부터 안쪽의 가로세로 길이.
    let d = 0; // 방향 시작 인덱스 : 하 우 상 좌

    for (let i = 0; i < cnt; i++) {
      tmp.push(g[sr][sc]);

      num[numCnt] = [sr, sc];
      [sr, sc] = [sr + dx[d], sc + dy[d]];
      if (!(start <= sr && sr < start + tn && start <= sc && sc < start + tm)) {
        [sr, sc] = [sr - dx[d], sc - dy[d]];
        d += 1;
        [sr, sc] = [sr + dx[d], sc + dy[d]];
      }
      numCnt += 1;
    }

    arr.push(tmp);
    start += 1;
    tn -= 2;
    tm -= 2;
  }
  // R번 회전해서 arr수정
  arr.forEach((array, idx) => {
    for (let i = 0; i < R % array.length; i++) {
      const a = array.pop();
      let tmp = [a, ...array];
      array = [...tmp];
    }
    arr[idx] = array;
  });
  // 회전한 결과를 g에 할당
  let prev = 0;
  arr.forEach((v, i) => {
    v.forEach((value, idx) => {
      const [x, y] = num[prev + idx];
      g[x][y] = value;
    });
    prev += v.length;
  });

  let answer = "";
  for (let i = 0; i < N; i++) {
    answer += g[i].map((e) => String(e)).join(" ");
    if (i < N - 1) answer += "\n";
  }

  console.log(answer);
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;
let M = null;
let R = null;
let g = [];
let count = 0;
rl.on("line", (line) => {
  if (!N) {
    [N, M, R] = line.split(" ").map((e) => +e);
  } else {
    g.push(line.split(" ").map((e) => +e));
    count += 1;
  }
  if (count === N) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 구현 문제
