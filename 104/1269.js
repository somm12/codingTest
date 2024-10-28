const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  // 이분 탐색을 통해 존재하는치 체크하고 공통 원소 개수 구하기
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);
  let cnt = 0;

  for (const target of A) {
    let [s, e] = [0, m - 1];

    while (s <= e) {
      const mid = parseInt((s + e) / 2);

      if (B[mid] === target) {
        cnt += 1;
        break;
      } else if (B[mid] < target) {
        s = mid + 1;
      } else {
        e = mid - 1;
      }
    }
  }
  console.log(n - cnt + m - cnt);
};
// 단순히 카운팅해서 1인 것만 찾아도 가능.
const solution2 = () => {
  const cnt = {};
  for (const v of A) {
    if (v in cnt) {
      cnt[v] += 1;
    } else {
      cnt[v] = 1;
    }
  }
  for (const v of B) {
    if (v in cnt) {
      cnt[v] += 1;
    } else {
      cnt[v] = 1;
    }
  }
  let answer = 0;
  const valueArr = Object.values(cnt);
  for (const v of valueArr) {
    if (v === 1) answer += 1;
  }
  console.log(answer);
};
let [n, m] = [null, null];
let [A, B] = [null, null];
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else if (!A) {
    A = line.split(" ").map((e) => +e);
  } else {
    B = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution2();
  process.exit();
});
// 백준 대칭 차집합.
