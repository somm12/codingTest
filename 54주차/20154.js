const solution = () => {
  let [minV, maxV] = [Infinity, 0];

  const combi = (s) => {
    // 세자리수이상일 때 세개의 수로 나누기.
    let arr = [];
    for (let i = 1; i < s.length - 1; i++) {
      for (let j = i + 1; j < s.length; j++) {
        let a = s.slice(0, i);
        let b = s.slice(i, j);
        let c = s.slice(j, s.length);
        arr.push(String(+a + +b + +c));
      }
    }
    return arr;
  };

  const dfs = (total, res, num) => {
    if (res.length === 1) {
      // 한자리 수가 되면 종료.
      if (res % 2 === 1) total += 1; // 홀수면 개수 추가.
      minV = Math.min(minV, total);
      maxV = Math.max(maxV, total);
      return;
    }
    let cnt = 0;
    for (let v of res) {
      // 현재 숫자의 각 자리수 홀수 개수 구하기.
      if (v % 2 === 1) cnt += 1;
    }
    // 자리수가 2개일 때, 각 자리수 더하기
    if (res.length === 2) dfs(total + cnt, String(+res[0] + +res[1]), num + 1);
    else {
      // 3개이상이면 임의의 세 수로 나누어서 각 수를 더한 수 만들기.
      for (let v of combi(res)) dfs(total + cnt, v, num + 1);
    }
  };

  dfs(0, N, 0);

  if (minV === Infinity) console.log(0, maxV);
  // 최솟값이 그대로면 0
  else {
    console.log(minV, maxV);
  }
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;

rl.on("line", (line) => {
  if (!N) {
    N = line;
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 20154.js
