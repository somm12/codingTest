const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  //0. 시간 복잡도는 2^(2*N)이 아니다. 행을 몇개 뒤집었을 때, 거기서 열을 뒤집고 말고가 필요한가?? => 행을 뒤집으면, 바로 열도 뒤집을지 말지 정해짐.
  // 즉, T개수가 많으면 뒤집는 것. 정해져있다. 따라서 행을 뒤집고말고의 모든 경우의 수 만으로도! T의 개수들은 알아서 최소를 만들 수 있다.
  // 1. 각 행을 숫자로 만들자.
  // 2. 뒤집고 안뒤집고 경우를 만드는 재귀함수 실행
  // 3. 모든 경우가 되면 즉 L == N 이 되면, 켜져있는가 확인을 통해 T의 개수를 구하고, n -cnt vs cnt 더 작은 것(뒤집고 말고) 더해서 최솟값 구하기.(즉여기서 열을 뒤집고 말고 경우가 포함된것.)
  const rowNum = Array(n).fill(0);
  let answer = Infinity;
  for (let i = 0; i < n; i++) {
    let value = 1;
    for (let j = 0; j < n; j++) {
      if (arr[i][j] == "T") rowNum[i] |= value;
      value *= 2;
    }
  }

  const dfs = (L) => {
    if (L == n) {
      let total = 0;
      for (let i = 1; i <= 1 << (n - 1); i *= 2) {
        let cnt = 0;

        for (let j = 0; j < n; j++) {
          if (rowNum[j] & i) cnt += 1;
        }

        total += Math.min(cnt, n - cnt);
      }
      answer = Math.min(total, answer);
      return;
    }
    dfs(L + 1);
    rowNum[L] = ~rowNum[L]; // 뒤집고 안뒤집고 차이.
    dfs(L + 1);
  };
  dfs(0);
  console.log(answer);
};

let n = null;
let cnt = 0;
let arr = [];
rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(line.split(""));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 동전 뒤집기.
