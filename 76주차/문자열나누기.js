const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const sol = () => {
  let answer = 0;
  const arr = [];
  let set = new Set();
  for (let i = 0; i < N - 2; i++) {
    // 3부분으로 나누기.
    const x = S.slice(0, i + 1);
    for (let j = i + 1; j < N - 1; j++) {
      const y = S.slice(i + 1, j + 1);
      const z = S.slice(j + 1, N);
      arr.push([x, y, z]);
      set.add(x);
      set.add(y);
      set.add(z);
    }
  }
  set = [...set]; // 중복제거 + 사전순 정렬.
  set.sort();

  for (let tmp of arr) {
    let total = 0;
    for (let v of tmp) {
      for (let i = 0; i < set.length; i++) {
        // 각 경우가 몇번째인지 체크 후, 점수 계산.
        if (set[i] == v) total += i + 1;
      }
    }
    answer = Math.max(answer, total); // 최댓값 반환.
  }
  console.log(answer);
};
let N;
let S;

rl.on("line", (line) => {
  if (!N) {
    N = +line;
  } else {
    S = line;
    rl.close();
  }
});

rl.on("close", () => {
  sol();
  process.exit();
});
