const isBingo = (r, c) => {
  let [ar, ac, adl, adr] = [[], [], [], []]; //각 행, 열, 대각선 왼쪽,오른쪽값들을 답을 배열
  let [cr, cc, cdl, cdr] = [0, 0, 0, 0]; // 행, 열, 대각선 지워진 개수 세기
  for (let i = 0; i < 5; i++) {
    if (mark[r][i] === "x") {
      cr += 1;
      ar.push(board[r][i]);
    }
    if (mark[i][c] === "x") {
      cc += 1;
      ac.push(board[i][c]);
    }
  }
  if (cr === 5) bingo[ar] = 1; //빙고 가로
  if (cc === 5) bingo[ac] = 1; //빙고 세로
  if (r === c) {
    //대각선 왼쪽 빙고
    for (let i = 0; i < 5; i++) {
      if (mark[i][i] === "x") {
        cdl += 1;
        adl.push(board[i][i]);
      }
    }
  }
  if (cdl === 5) bingo[adl] = 1;

  //대각선 오른쪽
  for (let i = 0; i < 5; i++) {
    if (mark[i][4 - i] === "x") {
      cdr += 1;
      adr.push(board[i][4 - i]);
    }
  }
  if (cdr === 5) bingo[adr] = 1;

  return Object.keys(bingo).length >= 3 ? true : false; //3개 이상되면 끝
};
const solution = () => {
  let num = {};
  mark = Array(5)
    .fill(0)
    .map((e) => Array(5).fill(0));
  for (let x = 0; x < 5; x++) {
    //숫자 지울 때 바로 위치를 찾기 위함.
    for (let y = 0; y < 5; y++) {
      num[board[x][y]] = [x, y];
    }
  }

  for (let i = 0; i < 25; i++) {
    const v = data[i];
    const [x, y] = num[v];
    mark[x][y] = "x";

    if (isBingo(x, y)) {
      console.log(i + 1);
      break;
    }
  }
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let mark = [];
let board = [];
let data = [];
let cnt = 0;
let bingo = {};

rl.on("line", (line) => {
  if (cnt < 5) {
    board.push(line.split(" ").map((e) => +e));
    cnt += 1;
  } else {
    let tmp = line.split(" ").map((e) => +e);
    data = [...data, ...tmp];
    cnt += 1;
  }
  if (cnt === 10) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 구현 문제
